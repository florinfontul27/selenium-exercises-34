'''
Test 2:
Deschidem https://the-internet.herokuapp.com/login
Dam click pe linkul Emental Selenium
Facem switch pe tabul urmator ( cautam pe net)
Facaem assert ca url-ul e corect - folosim ce am folosit in clasa pt celellate url-uri
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
chrome.find_element(By.LINK_TEXT, "Elemental Selenium").click()
sleep(10)
chrome.get("http://elementalselenium.com/")
assert chrome.current_url == "http://elementalselenium.com/"
chrome.quit()
