'''Test 5:
Deschidem https://the-internet.herokuapp.com/add_remove_elements/
Click pe butonul Add element
Click pe butonul de delete element
Assert ca buttonul de delete nu mai e displayed
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
chrome.find_element(By.CSS_SELECTOR,"#elements > button").click()
assert chrome.find_element(By.CSS_SELECTOR("#elements > button")).is_displayed()
if  is True:
    print("Element is dispalyed")
else:
    print("Element is not dispalyed")
chrome.quit()



