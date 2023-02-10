#librari gratuite care ne trebuie sa accesam selenium si sa avem acces la chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam chrome - un tab gol de chrome sau ce alt browser vrem
#salvam in variabila chrome tabul gol de chrome

# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# #maximaze window
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/login")
# username_input = chrome.find_element(By.ID, "username")
# username_input.send_keys("SuperSecretPassword!")
# chrome.find_element(By.ID, "password").send_keys("tomsmith")
# chrome.find_element(By.CLASS_NAME, "radius").click()
# assert chrome.current_url == "https://the-internet.herokuapp.com/login"
# error_message = chrome.find_element(By.ID, "flash")
# assert "Your username is invalid!" in error_message.text
# sleep(10)
# chrome.quit()

# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# #maximaze window
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/login")
# username_input = chrome.find_element(By.ID, "username")
# username_input.send_keys(" ")
# chrome.find_element(By.ID, "password").send_keys(" ")
# chrome.find_element(By.CLASS_NAME, "radius").click()
# assert chrome.current_url == "https://the-internet.herokuapp.com/login"
# error_message = chrome.find_element(By.ID, "flash")
# assert "Your username is invalid!" in error_message.text
# sleep(5)
# chrome.quit()

# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# #maximaze window
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/login")
# username_input = chrome.find_element(By.ID, "username")
# username_input.send_keys("fbcvbg%%^$$^*^%&")
# chrome.find_element(By.ID, "password").send_keys("^%$^%#$%")
# chrome.find_element(By.CLASS_NAME, "radius").click()
# assert chrome.current_url == "https://the-internet.herokuapp.com/login"
# error_message = chrome.find_element(By.ID, "flash")
# assert "Your username is invalid!" in error_message.text
# sleep(5)
# chrome.quit()

# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# #maximaze window
# username= "SuperSecretPassword!".upper()
# password = "tomsmith".upper()
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/login")
# username_input = chrome.find_element(By.ID, "username")
# username_input.send_keys(username)
# chrome.find_element(By.ID, "password").send_keys(password)
# chrome.find_element(By.CLASS_NAME, "radius").click()
# assert chrome.current_url == "https://the-internet.herokuapp.com/login"
# error_message = chrome.find_element(By.ID, "flash")
# assert "Your username is invalid!" in error_message.text
# sleep(5)
# chrome.quit()

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#maximaze window
password= "SuperSecretPassword!".upper()
username = "tomsmith"
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
username_input = chrome.find_element(By.ID, "username")
username_input.send_keys(username)
chrome.find_element(By.ID, "password").send_keys(password)
chrome.find_element(By.CLASS_NAME, "radius").click()
assert chrome.current_url == "https://the-internet.herokuapp.com/login"
error_message = chrome.find_element(By.ID, "flash")
assert "Your password is invalid!" in error_message.text
sleep(5)
chrome.quit()