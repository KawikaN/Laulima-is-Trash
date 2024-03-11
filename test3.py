# pip install undetected-chromedriver 
import undetected_chromedriver as uc 


# Initializing driver 
driver = uc.Chrome() 
 
# Try accessing a website with antibot service 
driver.get("https://authn.hawaii.edu/cas/login?service=https%3A%2F%2Flaulima.hawaii.edu%2Fsakai-login-tool%2Fcontainer&renew=true")
forms = driver.find_elements("xpath", "//form")
forms[0].find_element("username").send_keys("kawikakn")
forms[0].find_element("password").send_keys("Kanani99!")
forms[0].submit()
