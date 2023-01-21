'''Test 4:
Deschidem https://the-internet.herokuapp.com/add_remove_elements/
Click pe butonul Add element
Assert ca buttonul de delete e displayed
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
chrome.find_element(By.CSS_SELECTOR,"#content > div > button").click()
sleep(5)
delete_button = chrome.find_element(By.CSS_SELECTOR,"#elements > button")
assert delete_button.is_displayed(), "Check if delete button is displayed"
chrome.quit()
