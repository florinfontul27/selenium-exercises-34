# from time import sleep
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
#
# #salvam intr o variabila tab ul deschis
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.maximize_window()
# chrome.get("https://duckduckgo.com/")
# chrome.find_element(By.ID,"searchbox_input").send_keys("python")
# #pentru elemente de alte butoane de pe pagina inafara de litere sau cifre folosim libraria keys
# chrome.find_element(By.ID,"searchbox_input").send_keys(Keys.ENTER)
# sleep(5)
# chrome.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#salvam intr o variabila tab ul deschis
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://www.kfea.ro/cafea/")
chrome.find_element(By.ID,"search").send_keys("jacobs")
chrome.find_element(By.ID,"search").send_keys(Keys.ENTER)
sleep(10)
chrome.quit()
