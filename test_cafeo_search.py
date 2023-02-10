#librari gratuite care ne trebuie sa accesam selenium si sa avem acces la chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam chrome - un tab gol de chrome sau ce alt browser vrem
#salvam in variabila chrome tabul gol de chrome

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#maximaze window
chrome.maximize_window()
chrome.get("https://www.kfea.ro/cafea/")
chrome.find_element(By.ID, "search").send_keys("jacobs barista")
#pentru alte butoane de pe pagina inafara de literea sau cifre si caractere speciale folosim libraria keys
chrome.find_element(By.ID, "search").send_keys(Keys.ENTER)
#dupa ce dam search apar 25 rezultate - cand avem mai multe rezultate (daca da-mi cu Ctrl+7 si apar mai multe) si vrem sa facem ceva cu toate atunci
#folosim in loc de find_element find_elements - ne intoarce o lista cu toate elementele
lista_cautare = chrome.find_elements(By.CLASS_NAME, "snize-title")
#assert ca am primit 4 de rezultate dupa cautare
#e adevarat () trebuie sa fie ceva ce e True sau False. ca sa ne treaca testul trebuie sa fie acolo ceva True
# Daca e Fa   5>6, ==..un text egal cu alt text, lungimea unei liste sau al unui cuvant, sau a unei parole e egala cu un numar, element is displayed
assert len(lista_cautare) == 4
#assert ca toate rezultatele au in titlu jacobs barista (s-a facut cautarea corecta)
for web_element in lista_cautare:
    assert "jacobs barista" in web_element.text.lower()
chrome.quit()