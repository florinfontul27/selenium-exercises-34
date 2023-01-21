'''
Test 7:
Deschidem https://cafeo.ro/
Click pe Contul meu
Completati cu un email si parola gresita
Click intra in cont
Assert ca va apare textul din mesajul de eroare corect
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
chrome.find_element(By.CSS_SELECTOR, "#header_links > li.li_login.last > a").click()
username_input = chrome.find_element(By.CSS_SELECTOR, "#email")
username_input.send_keys("floringabi3@gmail.com")
chrome.find_element(By.CSS_SELECTOR,"#passwd").send_keys("SuperSecretPasswordDoi!")
chrome.find_element(By.CSS_SELECTOR,"#SubmitLogin > span > i").click()
sleep(10)
error_message = chrome.find_element(By.CSS_SELECTOR,"#center_column > div.alert.alert-danger > ol > li")
assert "Adresa de e-mail este invalida" in error_message.text
chrome.quit()
