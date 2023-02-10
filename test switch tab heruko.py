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
link_text = chrome.find_element(By.LINK_TEXT, "Elemental Selenium")
link_text.click()
sleep(2)
#am salvat taburile existente intr-o lista
#ca sa puteti da clic intr-un anumit tab, sa luati url-ul sau sa faceti orice pe pagina respectiva trebuie sa schimbati focusul pe tabul respectiv
lista_taburi = chrome.window_handles
chrome.switch_to.window(lista_taburi[1])
assert chrome.current_url == "http://elementalselenium.com/"
chrome.quit()