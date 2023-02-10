from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/dropdown")
select = Select(chrome.find_element(By.ID, "dropdown"))
sleep(5)
select.select_by_value("1")
sleep(5)
select.select_by_visible_text("Option 1")
sleep(5)
