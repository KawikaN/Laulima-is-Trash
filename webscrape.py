# webscraping the information on laulima

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import re
from flask import Flask, jsonify, Blueprint, request, redirect, url_for, render_template, session, json
import os
import random
import mechanicalsoup
#import bsObj

#parser = argparse.ArgumentParser(description="Login to GitHub.")
username = "kawikakn"
password = "Kanani99!"


browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)

browser.open("https://authn.hawaii.edu/cas/login?service=https%3A%2F%2Flaulima.hawaii.edu%2Fsakai-login-tool%2Fcontainer&renew=true")
browser.follow_link("login")
browser.select_form('#login form')
browser["login"] = username
browser["password"] = password
resp = browser.submit_selected()

browser.launch_browser()



# page_to_scrape2 = requests.get("https://wehewehe.org/gsdl2.85/cgi-bin/hdict?a=q&r=1&hs=1&m=-1&o=-1&qto=4&e=p-11000-00---off-0hdict--00-1----0-10-0---0---0direct-10-ED--4--textpukuielbert%252ctextmamaka-----0-1l--11-haw-Zz-1---Zz-1-home---00-3-1-00-0--4----0-0-11-00-0utfZz-8-00&q=" + find + "&fqv=textpukuielbert%252ctextmamaka&af=1&fqf=ED#hero-bottom-banner")
# sou2 = BeautifulSoup(page_to_scrape2.content, "html.parser")
# sou2.find_all('a', href=True)

##for text in msg2:
#definitions = [text.text for text in msg2]

