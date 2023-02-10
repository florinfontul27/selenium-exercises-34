#cum verificam ca un element nu e vizibil, cum folosim find_elements

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
chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
add_element_button = chrome.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
assert add_element_button.is_displayed()
add_element_button.click()
# delete_button = chrome.find_element(By.CSS_SELECTOR,'[onclick="deleteElement()"]')
# assert delete_button.is_displayed()
# delete_button.click()
# assert delete_button.is_displayed() == False
#o sa am o lista cu toate elementele ce au selectorul [onclick = ....
delete_button_list = chrome.find_elements(By.CSS_SELECTOR,'[onclick="deleteElement()"]')
assert delete_button_list[0].is_displayed()
assert len(delete_button_list) == 1
delete_button_list[0].click()
delete_button_list = chrome.find_elements(By.CSS_SELECTOR,'[onclick="deleteElement()"]')
#daca vreau sa verific ca un element nu mai e vizibil , verific ca lungimea liste e 0, ca nu mai am nici un webeleemnt cu seectorul respectiv
assert len(delete_button_list) == 0
#cum verifica ca am mai multe butone de delete element
for i in range(11):
    add_element_button.click()
delete_button_list = chrome.find_elements(By.CSS_SELECTOR,'[onclick="deleteElement()"]')
assert len(delete_button_list) == 11, "Number of delete button is not ok"
delete_button_list[10].click()
delete_button_list = chrome.find_elements(By.CSS_SELECTOR,'[onclick="deleteElement()"]')
assert len(delete_button_list) == 10, "Number of delete button is not ok"
delete_button_first = chrome.find_element()
# mesaj eroare cafeo  div[class="alert alert-danger"] > p
# ol > li
#center_column > div.alert.alert-danger > ol > li