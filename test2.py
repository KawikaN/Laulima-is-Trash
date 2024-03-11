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
#https://authn.hawaii.edu/cas/login?service=https%3A%2F%2Flaulima.hawaii.edu%2Fsakai-login-tool%2Fcontainer&renew=true
browser.open("https://authn.hawaii.edu/cas/login?service=https%3A%2F%2Flaulima.hawaii.edu%2Fsakai-login-tool%2Fcontainer&renew=true")
#browser.follow_link("loginForm")
#browser.select_form('#login form')
browser.select_form(nr=0)
browser["username"] = "kawikakn"
browser["password"] = "Kanani99!"
resp = browser.submit_selected()

# Uncomment to launch a web browser on the current page:
browser.launch_browser()

# verify we are now logged in


# verify we remain logged in (thanks to cookies) as we browse the rest of
# the site
