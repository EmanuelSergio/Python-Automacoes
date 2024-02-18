import pyautogui 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import difflib

url = 'https://www.cifraclub.com.br/'

nomeMusica = 'Another Love - Tom Odell - Cifra Club'
senha = 'ttrtt'

driver = webdriver.Chrome()


def verificar_semelhanca(str1, str2):
    # Normaliza as strings para evitar problemas de maiúsculas/minúsculas
    str1 = str1.lower()
    str2 = str2.lower()

    # Calcula a razão de similaridade
    similarity_ratio = difflib.SequenceMatcher(None, str1, str2).ratio()

    # Define um limite de similaridade (ajuste conforme necessário)
    limite_similaridade = 0.8

    # Retorna True se a similaridade for maior que o limite
    return similarity_ratio > limite_similaridade

try:
    
    
    driver.get(url)
    
   
    
    

    username_field = driver.find_element(By.ID, 'js-h-search')
    username_field.send_keys(nomeMusica)
    
    time.sleep(3)
    
    botao_pesquisa = driver.find_element(By.CLASS_NAME,'header-searchButton')
    botao_pesquisa.click()
    
    resultados = driver.find_elements(By.CLASS_NAME,'gs-title')


    
    for resultado in resultados:
           
     if resultado.text == nomeMusica:
           resultado.click()
           time.sleep(2)
         

   
    

    
    
    
finally:  
    
    time.sleep(4)



"""""

pyautogui.PAUSE = 1 #vai executar cada comando a cada 1 segundos

#abrir a ferramente/sistema/programa para fazer o login
pyautogui.press('win')  
pyautogui.write('google') #se nao achar o arquivo de primeira, coloca pra apertar o backspace
pyautogui.press('enter')

pyautogui.click(x=1424, y=103)
pyautogui.click(x=1323, y=475)
pyautogui.write('10089717902')
pyautogui.click(x=1531, y=550)



time.sleep(3)
print(pyautogui.position())
"""