'''
Test 6:
Deschidem https://the-internet.herokuapp.com/add_remove_elements/
Click pe butonul Add element de 10 ori (folosind un for)
Folosind find_elements  faceti un assert ca sunt 10 butoane de delete
(v-am pus un exemplu in ce am facut la clasa cu find_elements
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
chrome.quit()