from selenium import webdriver
from selenium.webdriver.common.by import By
import config

# Create an chrome class instance
browser = webdriver.Chrome()

# Get the browser and open the url 
browser.get("https://realpython.com/")

# Find sign in text by it's element and click on it
signin_link = browser.find_element(by=By.LINK_TEXT, value="Sign‑In")
signin_link.click()

# Find element on user email and pass input and write the info
user_email = browser.find_element(By.ID, "id_login")
user_email.send_keys(config.user_email)

password = browser.find_element(By.ID, "id_password")
password.send_keys(config.password)

# Submit the form and get login
password.submit()

# Click on the profile avatar and then click on the Manage Account
avatar = browser.find_element(By.CLASS_NAME, "align-self-center")
avatar.click()

# Click on the Manage Account item in the dropdown
manage_account = browser.find_element(By.LINK_TEXT, "Manage Account")
manage_account.click()

# Get user name element on profile page store in user_name variable
user_name = browser.find_element(By.TAG_NAME, "strong")

user_name_label = user_name.get_attribute("innerHTML")
   
# Assert the text "khalid280284" is in the user_name_lable
assert "khalid280284" in user_name_label

# Logging out
browser.find_element(By.CLASS_NAME, "align-self-center").click()

# Tray opens and find element for log out button then click on it
logout_button = browser.find_element(By.LINK_TEXT, "Sign Out")
logout_button.click()

# Log out confirm page find element for confirm logout button and click on it
confirm_signout = browser.find_element(By.CLASS_NAME, "btn-danger")
confirm_signout.click()

# Public page has a alert message that you logged out, get the innerHTML of this element then assert that the message text in rendered in the html
alert_msg = browser.find_element(By.CLASS_NAME, "alert-dismissible")
alert_msg_label = alert_msg.get_attribute("innerHTML")

assert "You have signed out." in alert_msg_label

browser.quit()
