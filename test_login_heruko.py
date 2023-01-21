#daca functioneaza butonul de login
#textele de pe pagina

#daca ne lasa sa scriem text-daca ne permite sa scriem caractere speciale
#daca merge sa ne logam cu id sau parola gresite
#daca exista o limita inferioara/superioara de caractere
#testare negativa
#bagam un username cu caractere speciale
#daca schimbam intre ele username si parola si merge
#daca ne logam si delogam si logam iar
#daca dupa ce ne logam ne raman datele salvate
#daca ne logam si dupa dam refresh
#merge linkul emenatal selenium



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
username_input = chrome.find_element(By.ID, "username")
username_input.send_keys("tomsmith")
chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
chrome.find_element(By.CLASS_NAME, "radius").click()
#sau alta varianta cu css selector
#la clasa punem punct in fata
#chrome.find_element(By.CSS_SELECTOR, ".radius")
sleep(10)
#verificari
# logout_button = chrome.find_element(By.CSS_SELECTOR, "[href='/logout']")
# logout_button = chrome.find_element(By.CLASS_NAME, "button secondary radius")
logout_button = chrome.find_element(By.CSS_SELECTOR, "[class='button secondary radius']")
# logout_button = chrome.find_element(By.CSS_SELECTOR, "[#content > div > a]")
# logout_button = chrome.find_element(By.XPATH, "[//*[@id="'content'"]/div/a]")
#butonul de log out
assert logout_button.is_displayed(), "check if logout button is displayed"
#butonul de log out
#mesajul de welcome
#text_welcome = chrome.find_element(By.CLASS_NAME,"subheader")
text_welcome = chrome.find_element(By.TAG_NAME,"h4")
# cu .text luam textul negru din element
assert text_welcome.text == "Welcome to the Secure Area. When you are done click logout below."
#mesajul you logged in a secure area
flash_message = chrome.find_element(By.ID,"flash")
assert "You logged into a secure area!" in flash_message.text
assert chrome.current_url == "https://the-internet.herokuapp.com/login"
#current_url iti ia url ul curent de sus
chrome.quit()