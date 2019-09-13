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
driver.execute_script("window.open('https://api.whatsapp.com/send?phone=5493513883708&text=Como%20estas%20inscripta%20en%20el%20Programa%20bajo%20la%20modalidad%20CTI%2c%20deb%c3%a9s%20presentar%20el%20alta%20temprana%20de%20AFIP%20lo%20antes%20posible.%20Ten%c3%a9%20en%20cuenta%20que%20de%20acuerdo%20a%20la%20fecha%20en%20que%20presentes%20el%20documento%20de%20AFIP%2c%20se%20empezar%c3%a1%20a%20gestionar%20el%20tr%c3%a1mite%20de%20pago.%20%c2%a1Saludos%21&source=&data=');")


