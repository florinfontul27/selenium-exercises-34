#initializam chrome ul - un tab gol de chrome sau ce alt browser vrem
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



#salvam intr o variabila tab ul deschis
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
sleep(5)
#daca elementul e de tip a, folosim by_link_text si copiem textul cu negru
chrome.find_element(By.LINK_TEXT, "Elemental Selenium").click()
sleep(12)
chrome.quit()
