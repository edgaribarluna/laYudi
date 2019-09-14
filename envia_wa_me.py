from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
import openpyxl as excel

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com/')
input("apreta algun boton luego de escanear el QR")

driver.execute_script("window.location.href = 'https://web.whatsapp.com/send?phone=5493513883708&text=Cjhghj';")

no_encuentra = driver.find_elements_by_xpath("//*[contains(text(), 'El número de teléfono compartido a través de la dirección URL es inválido')]")
  
#//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div

#//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]
