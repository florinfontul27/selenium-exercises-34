'''
Test 3:
Deschidem https://the-internet.herokuapp.com/login
Ne logam cu user si parola corecta
Dam click pe Logout
Assert ca suntem pe paagina de logare (2 verificari care vreti voi)
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
username_input = chrome.find_element(By.ID, "username")
username_input.send_keys("tomsmith")
chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
chrome.find_element(By.CLASS_NAME, "radius").click()
logout_button = chrome.find_element(By.CSS_SELECTOR, "[class='button secondary radius']")
assert logout_button.is_displayed(), "check if logout button is displayed"
text_welcome = chrome.find_element(By.TAG_NAME,"h4")
assert text_welcome.text == "Welcome to the Secure Area. When you are done click logout below."
sleep(5)
chrome.quit()