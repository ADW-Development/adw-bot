import requests

URLchecks = []

'''
Add urls that need to be checked here.
example: https://adw-development.github.io/newpage
'''

print("conducting url checks...")

for url in URLchecks:
    try:
        main_response = requests.get(url)
        if main_response.status_code == 200:
            print(f"The page: {url} exists")
        else:
            print(f"The page: {url} has an error. Check the HTML or CSS. HTTP status: {main_response.status_code}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred while checking the URL: {error}")
