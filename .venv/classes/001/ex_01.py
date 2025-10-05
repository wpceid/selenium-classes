# Exercício Prático: Fazendo uma Busca no Google
# Exercicio dado em aula

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  # Corrigido import
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By  # Necessário para localizar elementos

# Abrindo o navegador e definindo a espera
nav = webdriver.Chrome()
nav.maximize_window()
espera = WebDriverWait(nav, 5)  # Corrigido: vírgula e não ponto

# Abrindo o site do google
nav.get("https://www.google.com")

# Esperando o campo de busca estar presente
#espera.until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

# Escrevendo a busca
campo_busca = nav.find_element(By.CLASS_NAME, "gLFyf")
campo_busca.send_keys("Selenium Python")
campo_busca.send_keys(Keys.ENTER)

time.sleep(100000)

