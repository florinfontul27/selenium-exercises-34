'''Alegeti-va unu sau mai multe din sugestiile de site-uri de mai jos
https://www.phptravels.net/
http://automationpractice.com/index.php
https://formy-project.herokuapp.com/
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html
jules.app
Alegeti cate 3 elemente din fiecare tip de selector din urmatoarele categorii:
Id
Link text
Partial link text
Name
Tag
Class name*
obs:
Probabil nu veti gasi un singur website care sa cuprinda toate variantele de mai sus, astfel ca va recomandam sa folositi mai multe site-uri
Optional: La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista
'''

'''Am ales https://www.phptravels.net/'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://www.phptravels.net/")
sleep(5)

chrome.quit()