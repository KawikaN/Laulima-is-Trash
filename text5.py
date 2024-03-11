import undetected_chromedriver as uc 
import selenium
from bs4 import BeautifulSoup
import mechanicalsoup
import time
from bs4 import BeautifulSoup
import requests


# Initializing driver 
driver = uc.Chrome() 
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

time.sleep(0.5)

current_url = driver.current_url



    
while(all(char in current_url for char in "duosecurity")):
    print("Please push")
    time.sleep(2)

    # page = requests.get(driver.current_url)
    # soup = BeautifulSoup(page.content, "html.parser")
    # print(soup.find_all('h1'))
    # print( driver.find_element("xpath", "//*[text()='Yes, this is my device']") )
    #("xpath", "//input[@id='trust-this-browser-label']"))



soup = BeautifulSoup(driver.current_url, "html.parser")
driver.quit()


#https://api-16a593a9.duosecurity.com/frame/v4/auth/prompt?sid=frameless-fb44a5ce-f1c4-4343-be15-dae20b50a0a7
#https://api-16a593a9.duosecurity.com/frame/v4/auth/prompt?sid=frameless-fb44a5ce-f1c4-4343-be15-dae20b50a0a7
#trust-browser-button
#<button id="trust-browser-button" class="button--primary--full-width button--primary button--xlarge size-margin-top-xlarge size-margin-bottom-medium">Yes, this is my device</button>

<script id="base-data" type="text/json">{"brand": {"company": "Duo Security", "desktop": "Duo Desktop", "mobile": "Duo Mobile", "id": "duo", "website_root": "https://duo.com", "product": "Duo", "push": "Duo Push"}, "help_url": "https://guide.duo.com/traditional-enrollment", "logo": {"logo_link": "/frame/prompt?sid=frameless-32fe69c6-b6f9-4bec-a9bf-14b7bfe07268", "logo_alt_text": "Duo Security Logo", "logo_src": "/frame/static/img/duo-cisco-logo-green.png?v=437f1"}, "session_id": "frameless-32fe69c6-b6f9-4bec-a9bf-14b7bfe07268", "use_duo_branding": true, "const": {"factor_phone": "Phone Call", "factor_passcode": "Passcode", "factor_push": "Duo Push", "device_u2f": "u2f", "device_webauthn": "webauthn", "post_auth_add_device": "addDevice", "post_auth_manage_devices": "manageDevices", "os_families": ["Windows Phone", "Blackberry", "Mac OS X", "Windows", "iOS", "Android", "Linux", "Chrome OS", "Unknown Operating System"], "browser_families": ["Safari", "Chrome", "Firefox", "Internet Explorer", "Edge", "Mobile Safari", "Chrome Mobile", "Opera", "Opera Mobile", "Firefox Mobile", "Unknown", "Edge Chromium", "Edge Chromium Mobile"], "software_family_chrome": "Chrome"}, "is_new_user": false, "show_self_service_links": false, "helpdesk_message": "null", "is_in_oidc_flow": true, "xsrf_token": "fdc11bec7c0348edaa63039dc11ff5e7", "style": {"app_background_color": "#E7E9ED", "accent_color": "#0B69E5"}, "features": {"has_webauthn_browser_expansion_feature": false, "has_hostname_validation_feature": false, "has_auto_selection_feature": false, "has_device_filter_feature": false, "has_iframed_up_blocking_feature": false}, "session_trace": "", "can_offer_new_device_flow": false}</script>

<script id="base-data" type="text/json">{"brand": {"company": "Duo Security", "desktop": "Duo Desktop", "mobile": "Duo Mobile", "id": "duo", "website_root": "https://duo.com", "product": "Duo", "push": "Duo Push"}, "help_url": "https://guide.duo.com/traditional-enrollment", "logo": {"logo_link": "/frame/prompt?sid=frameless-32fe69c6-b6f9-4bec-a9bf-14b7bfe07268", "logo_alt_text": "Duo Security Logo", "logo_src": "/frame/static/img/duo-cisco-logo-green.png?v=437f1"}, "session_id": "frameless-32fe69c6-b6f9-4bec-a9bf-14b7bfe07268", "use_duo_branding": true, "const": {"factor_phone": "Phone Call", "factor_passcode": "Passcode", "factor_push": "Duo Push", "device_u2f": "u2f", "device_webauthn": "webauthn", "post_auth_add_device": "addDevice", "post_auth_manage_devices": "manageDevices", "os_families": ["Windows Phone", "Blackberry", "Mac OS X", "Windows", "iOS", "Android", "Linux", "Chrome OS", "Unknown Operating System"], "browser_families": ["Safari", "Chrome", "Firefox", "Internet Explorer", "Edge", "Mobile Safari", "Chrome Mobile", "Opera", "Opera Mobile", "Firefox Mobile", "Unknown", "Edge Chromium", "Edge Chromium Mobile"], "software_family_chrome": "Chrome"}, "is_new_user": false, "show_self_service_links": false, "helpdesk_message": "null", "is_in_oidc_flow": true, "xsrf_token": "18281a51cdc04421ae41b1e9d1798d03", "style": {"app_background_color": "#E7E9ED", "accent_color": "#0B69E5"}, "features": {"has_webauthn_browser_expansion_feature": false, "has_hostname_validation_feature": false, "has_auto_selection_feature": false, "has_device_filter_feature": false, "has_iframed_up_blocking_feature": false}, "session_trace": "", "can_offer_new_device_flow": false}</script>