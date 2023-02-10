'''
Test 1:
Deschideti https://cafeo.ro/
Click contul meu
Click cont nou
Verificati mesajul de eroare
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
sleep(5)
chrome.find_element(By.CSS_SELECTOR,"#header_links > li.li_login.last > a > i").click()
chrome.find_element(By.CSS_SELECTOR,"#SubmitCreate > span").click()
lista_taburi = chrome.window_handles
chrome.switch_to.window(lista_taburi[1])
assert chrome.current_url == "https://cafeo.ro/autentificare?back=my-account"
sleep(4)
error_message = chrome.find_element(By.ID,"#create_account_error")
assert "Adresa de e-mail este invalida" in error_message.text
sleep(5)
chrome.quit()

