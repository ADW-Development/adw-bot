import time
import requests
from urllib.parse import urlparse, urlunparse

URLchecks = ["https://adw-development.github.io/teddy.html", "https://adw-development.github.io/"] # or whatever. replace with the urls you need to check.

headers = {
    "User-Agent": "ADW-bot"
}

def is_allowed_by_robots(robots_txt, user_agent, path="/"):
    allowed = True
    process_rules = False
    for line in robots_txt.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.lower().startswith("user-agent:"):
            agent = line.split(":", 1)[1].strip()
            process_rules = (agent == "*" or agent.lower() == user_agent.lower())
        elif process_rules:
            if line.lower().startswith("disallow:"):
                rule = line.split(":", 1)[1].strip()
                if rule == "" or path.startswith(rule):
                    allowed = False
            elif line.lower().startswith("allow:"):
                rule = line.split(":", 1)[1].strip()
                if path.startswith(rule):
                    allowed = True
        # Stop processing rules if a new user-agent block starts
        if line.lower().startswith("user-agent:") and process_rules and agent.lower() != user_agent.lower():
            break
    return allowed

print("Conducting URL checks...")

for url in URLchecks:
    try:
        parsed = urlparse(url)
        robots_url = urlunparse((parsed.scheme, parsed.netloc, '/public/robots.txt', '', '', ''))
        robots_response = requests.get(robots_url, headers=headers)
        if robots_response.status_code == 200:
            print(f"robots.txt found at {robots_url}")
            if is_allowed_by_robots(robots_response.text, headers["User-Agent"], parsed.path):
                print(f"ADW-bot is allowed to crawl {url}")
                main_response = requests.get(url, headers=headers)
                if main_response.status_code == 200:
                    print(f"The URL: {url} was successfully reached. no errors while doing so.")
                else:
                    print(f"The page: {url} has an error. HTTP status: {main_response.status_code}")
            else:
                print(f"ADW-bot is NOT allowed to crawl {url} (disallowed by robots.txt)")
        else:
            print(f"robots.txt not found at {robots_url} (HTTP {robots_response.status_code}), proceeding anyway.")
            main_response = requests.get(url, headers=headers)
            if main_response.status_code == 200:
                print(f"The URL: {url} was successfully reached. no errors while doing so.")
            else:
                print(f"The page: {url} has an error. HTTP status: {main_response.status_code}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred while checking the URL: {error}")

time.sleep(10)
