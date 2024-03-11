import undetected_chromedriver as uc 
import selenium
from bs4 import BeautifulSoup
import mechanicalsoup
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver



# Initializing driver 
driver = uc.Chrome(headless=True) 
options = uc.ChromeOptions()
#headless=True


# Try accessing a website with antibot service 
driver.get("https://authn.hawaii.edu/cas/login?service=https%3A%2F%2Flaulima.hawaii.edu%2Fsakai-login-tool%2Fcontainer&renew=true")

# Find the username and password input fields and submit button using XPath
username_input = driver.find_element("xpath", "//input[@name='username']")
password_input = driver.find_element("xpath", "//input[@name='password']")

#submitBtn
# Enter username and password
username_input.send_keys("kawikakn")
password_input.send_keys("Kanani99!")
z=driver.find_element("xpath", '//*[@name="submitBtn"]')
#z=driver.find_element_by_xpath("//input[@name='submitBtn']")
z.click()

time.sleep(1)


current_url = driver.current_url
response = requests.get(current_url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

# checks if its on the pushing screen or if we were pushed through
while(True):
    out_of_stock_text = "your"
    if out_of_stock_text in driver.page_source:
        break
    else:
        print("Please push the duo")
        time.sleep(2)
        continue


current_url = driver.current_url
response = requests.get(current_url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
driver.find_element("xpath", '//*[@id="trust-browser-button"]').click()

while(True):
    continue


#<a class="Mrphs-toolsNav__menuitem--link " href="https://laulima.hawaii.edu/portal/site/%7Ekawikakn/tool/64f8588c-52ca-4e25-8d17-1c4c67a6b2a6" title="Membership - For viewing and modifying your membership in sites of which you are a participant or that you may join">
        # <div class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-membership   "></div>
        #     			<div class="Mrphs-toolsNav__menuitem--title">Membership</div>
		# 				<div class="Mrphs-toolsNav__menuitem--status-block">
		# 									</div>
		# </a>



# while(True):
#     a = soup.find_all('a')
#     print(a)

driver.quit()

