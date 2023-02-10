'''
Test 2:
Deschideti https://cafeo.ro/
Click contul meu
Completati  cu o adresa de email
Click cont nou
Fara sa completati nimic dati click creare cont
Assert pe mesajul de eroare
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://cafeo.ro/")
chrome.find_element(By.CSS_SELECTOR,"#header_links > li.li_login.last > a > i").click()
email_adress_input = chrome.find_element(By.CSS_SELECTOR, "#email_create")
email_adress_input.send_keys("floringabi3@gmail.com")
chrome.find_element(By.CSS_SELECTOR, "#email_create").send_keys("floringabi3@gmail.com")
sleep(4)
chrome.find_element(By.CSS_SELECTOR,"#create-account_form > div > div.submit").click()
sleep(15)
chrome.find_element(By.CSS_SELECTOR,"#create-account_form > div > div.submit").click()
error_message = chrome.find_element(By.CSS_SELECTOR,"create_account_error")
assert "Adresa de e-mail este invalida" in error_message.text
chrome.quit()
