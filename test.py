"""Example app to login to GitHub using the StatefulBrowser class.

NOTE: This example will not work if the user has 2FA enabled."""

import argparse
from getpass import getpass

import mechanicalsoup





browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)
# Uncomment for a more verbose output:
# browser.set_verbose(2)

browser.open("https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FKawikaN")
#browser.follow_link("login")
browser.select_form('#login form')
browser["login"] = "kknjr16@gmail.com"
browser["password"] = "Kealoha96792!@"
resp = browser.submit_selected()

# Uncomment to launch a web browser on the current page:
browser.launch_browser()

# verify we are now logged in


# verify we remain logged in (thanks to cookies) as we browse the rest of
# the site
