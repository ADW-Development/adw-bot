# URL Availability Checker

A Python script that checks URL availability while respecting `robots.txt` rules, designed for ADW developers and web developers who need to verify the accessibility of their web content.

# Features

- Checks multiple URLs for availability
- Respects `robots.txt` rules before crawling
- Custom user-agent support (ADW-bot)
- Detailed status reporting for each URL
- Error handling for network issues

# Requirements

- Python 3.x
- `requests` library

# Installation

1. Clone this repository or download the script
2. Install the required dependencies:
   ```bash
   pip install requests

# Usage
1. Edit the URLchecks list in the script to include the URLs you want to check
2. Run the script:

bash
```
python bot.py
```

The script will:
+ Attempt to find and parse robots.txt for each domain
+ Check if the ADW-bot is allowed to crawl each URL
+ Report whether each URL is accessible or returns an error
+ Wait 10 seconds between checks (adjustable in the code)

# Sample Output

bash
```
Conducting URL checks...
robots.txt found at https://adw-development.github.io/public/robots.txt
ADW-bot is allowed to crawl https://adw-development.github.io/teddy.html
The URL: https://adw-development.github.io/teddy.html was successfully reached. no errors while doing so.
robots.txt found at https://adw-development.github.io/public/robots.txt
ADW-bot is allowed to crawl https://adw-development.github.io/
The URL: https://adw-development.github.io/ was successfully reached. no errors while doing so.
```

# Customization
+ Modify the sleep time at the end of the script (if you want to)

+ Add additional URL checks to the URLchecks list (becuase, you need to replace the whole thing.)
