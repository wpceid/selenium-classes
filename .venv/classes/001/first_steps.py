#Este arquivo foi criado para fins de estudos baseado na aula disponivel neste vídeo https://www.youtube.com/watch?v=71ECrViH_Ng

from selenium import webdriver
import time

#abrir o navegador
navegador = webdriver.Chrome()
navegador.maximize_window()

#acessar um site
navegador.get("https://www.google.com.br")

#esperar 10s para fechar
time.sleep(10)