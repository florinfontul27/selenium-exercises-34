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
sleep(3)
#by id
username_input = chrome.find_element(By.ID, "username")
username_input.send_keys("tomsmith")
chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(3)
#by class - ne folosim de atributul class
chrome.find_element(By.CLASS_NAME, "radius").click()
sleep(15)


#ne inchide fereastra de chrome
chrome.quit()
#in proiectul final nu putem sleep, asta e doar pt noi ca sa vedem
