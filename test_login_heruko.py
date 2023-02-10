#daca functioneaza butonul login
#textele de pe pagina - de facut acasa

# daca ne permite sa scriem caractere speciale

#daca exista limitainferioara/superioara de caractere

#testare negativa
#bagam un usernam cu caactere special
#daca schimbam intre ele username cu parola daca merge
#daca merge sa ne logam cu id/parola gresit

#daca ne logam si delogam si logam iar
#daca dupace ne logam ne raman datele salvate
#daca dam logout si apoi refresh
#textele de pe pagina
#merge linkul de emental selenium


#librari gratuite care ne trebuie sa accesam selenium si sa avem acces la chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam chrome - un tab gol de chrome sau ce alt browser vrem
#salvam in variabila chrome tabul gol de chrome

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#maximaze window
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
username_input = chrome.find_element(By.ID, "username")
username_input.send_keys("tomsmith")
chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
chrome.find_element(By.CLASS_NAME, "radius").click()

#sau alta varianta cu css selector
#la clasa puneti . in fata
# chrome.find_element(By.CSS_SELECTOR, ".radius")
sleep(10)
#verificari
#content > div > a
# logout_button = chrome.find_element(By.CSS_SELECTOR, "[href='/logout']")
#daca are numele la clasa mai lung decat un cuvant si e saptiu intre cuvinte nu merge cu by classnamelogout_button = chrome.find_element(By.CLASS_NAME, "button secondary radius")
logout_button = chrome.find_element(By.CSS_SELECTOR, "[class='button secondary radius']")
# logout_button = chrome.find_element(By.CSS_SELECTOR, "#content > div > a")
# logout_button = chrome.find_element(By.XPATH, "//*[@id='content']/div/a")
#butonul de logout
assert logout_button.is_displayed(), "Check logout button is displayed"
#mesajul de welcome
#text_welcome = chrome.find_element(By.CLASS_NAME, "subheader")
text_welcome = chrome.find_element(By.TAG_NAME, "h4")
#cu .text luam textul negru din element
assert text_welcome.text == "Welcome to the Secure Area. When you are done click logout below."
#mesajul you logged in a secure area
flash_message = chrome.find_element(By.ID, "flash")
assert "You logged into a secure area!" in flash_message.text
#current_url iti ia url-ul curent de sus
assert chrome.current_url == "https://the-internet.herokuapp.com/secure"
chrome.quit()