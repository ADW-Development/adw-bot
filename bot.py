import requests

URLchecks = []

'''
Add URLs that need to be checked here.
Example: https://adw-development.github.io/newpage
'''

print("Conducting URL checks...")

for url in URLchecks:
    try:
        main_response = requests.get(url)
        if main_response.status_code == 200:
            print(f"The URL: {url} exists")
        else:
            print(f"The page: {url} has an error. HTTP status: {main_response.status_code}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred while checking the URL: {error}")
