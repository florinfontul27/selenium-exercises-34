from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



#salvam intr o variabila tab ul deschis
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/login")
# username_input = chrome.find_element(By.ID, "username")
# username_input.send_keys("SuperSecretPassword!")
# chrome.find_element(By.ID, "password").send_keys("tomsmith!")
# chrome.find_element(By.CLASS_NAME, "radius").click()
# sleep(10)
# assert chrome.current_url == "https://the-internet.herokuapp.com/login"
# error_message = chrome.find_element(By.ID,"flash")
# assert "Your username is invalid!" in error_message.text
# chrome.quit()


# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/login")
# username_input = chrome.find_element(By.ID, "username")
# username_input.send_keys(" ")
# chrome.find_element(By.ID, "password").send_keys(" ")
# chrome.find_element(By.CLASS_NAME, "radius").click()
# sleep(10)
# assert chrome.current_url == "https://the-internet.herokuapp.com/login"
# error_message = chrome.find_element(By.ID,"flash")
# assert "Your username is invalid!" in error_message.text
# chrome.quit()
#
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://the-internet.herokuapp.com/login")
# username_input = chrome.find_element(By.ID, "username")
# username_input.send_keys("fdfdsdscsfdfd%$#$##")
# chrome.find_element(By.ID, "password").send_keys("$#@$#$@#$")
# chrome.find_element(By.CLASS_NAME, "radius").click()
# sleep(10)
# assert chrome.current_url == "https://the-internet.herokuapp.com/login"
# error_message = chrome.find_element(By.ID,"flash")
# assert "Your username is invalid!" in error_message.text
# chrome.quit()

username = "SuperSecretPassword!".upper()
password = "tomsmith".upper()
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
username_input = chrome.find_element(By.ID, "username")
username_input.send_keys(username)
chrome.find_element(By.ID, "password").send_keys(password)
chrome.find_element(By.CLASS_NAME, "radius").click()
sleep(10)
assert chrome.current_url == "https://the-internet.herokuapp.com/login"
error_message = chrome.find_element(By.ID,"flash")
assert "Your username is invalid!" in error_message.text
chrome.quit()