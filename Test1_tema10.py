'''Test1 :
Deschidem https://the-internet.herokuapp.com/login
Assert ca textul de la titlu e corect
Assert ca textul lung e corect
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
title_text = chrome.find_element(By.TAG_NAME,"h2")
assert title_text.text == "Login Page"
long_text = chrome.find_element(By.CLASS_NAME,"subheader")
assert long_text.text == "This is where you can log into the secure area. Enter tomsmith for the username and SuperSecretPassword! for the password. If the information is wrong you should see error messages."
sleep(5)
chrome.quit()