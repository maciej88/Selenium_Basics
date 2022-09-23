from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='./chromedriver')

chrome_browser = webdriver.Chrome(service=service)

chrome_browser.maximize_window()

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title
button_add = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
print(button_add.get_attribute('innerHTML'))

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('Light weight!')

button_add.click()
