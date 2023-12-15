from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/")

user_name_box = browser.find_element(By.ID, "user-name")
user_name_box.send_keys("standard_user")
password_box = browser.find_element(By.ID, "password")
password_box.send_keys("secret_sauce")
password_box.submit()

title = browser.find_element(By.CLASS_NAME, "app_logo")

page_title = title.get_attribute("innerHTML")
print(page_title)

assert "Swag Labs" in page_title
