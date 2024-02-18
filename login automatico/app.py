import pyautogui 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://sso.acesso.gov.br/login?client_id=www.gov.br&authorization_id=18c3b75ba3f'

cpf = '654324663'
senha = 'ttrtt'

driver = webdriver.Chrome()

try:
    
    
    driver.get(url)
    
   
    botao_login = driver.find_element(By.ID, 'barra-sso')    
    botao_login.click()
    

    
    
    time.sleep(2)
    
    username_field = driver.find_element(By.ID, 'accountId')
    username_field.send_keys(cpf)
    
    username_field.send_keys(Keys.RETURN)
    
    time.sleep(10)
    
    password_field = driver.find_element(By.CLASS_NAME, 'password')
    password_field.send_keys(senha)
    
    
    
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