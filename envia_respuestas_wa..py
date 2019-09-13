# envia_respuestas_wa.py

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import openpyxl as excel

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com/')
input("apreta algun boton luego de escanear el QR")
i = 0


def busca_elemetos():

  text = ''
  textfinder1 = driver.find_elements_by_class_name('_3La1s')
  for i in textfinder1:
    text += i.text + '\n'
  print(text)


def envia_mensaje(contact, text):
  inp_xpath_search = "//input[@title='Buscar o empezar un chat nuevo']"
  input_box_search = WebDriverWait(driver, 50).until(
      lambda driver: driver.find_element_by_xpath(inp_xpath_search))
  input_box_search.click()
  time.sleep(2)

  input_box_search.send_keys(contact + Keys.ENTER)
  time.sleep(4)

  # no_encuentra = driver.find_elements_by_xpath("//*[contains(text(), 'Buscando chats, contactos y mensajes...')]")
  no_encuentra2 = driver.find_elements_by_xpath("//*[contains(text(), 'No se encontró ningún chat, contacto ni mensaje')]")
  error = bool(no_encuentra2) 
  if error == True:
      print(contact + "Oops! no esta ese contacto...")
      ws['D' + str(i)] = "no enviado"
      time.sleep(2)
      bot_clear = '//button[@class="_2heX1"]'
      try:
          boton_clear = driver.find_element_by_xpath(bot_clear)
          time.sleep(2)
          boton_clear.click()
      except NoSuchElementException:  # spelling error making this code not work as expected
          pass
      file.save("contacts.xlsx")
      time.sleep(2)  
  else:
          # selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
          # selected_contact.send_keys(keys.ENTER)
          inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'

          input_box = driver.find_element_by_xpath(inp_xpath)
          ws['D' + str(i)] = "enviado"
          time.sleep(2)
          input_box.send_keys(text + Keys.ENTER)
          time.sleep(2)
          file.save("contacts.xlsx")
          return
  return


file = excel.load_workbook(filename = "contacts.xlsx")
ws = file.active


for row in ws.values:
  i = i + 1
  contacto =str(row[0])
  texto = " " + row[1] +", " + row[2]
  # print(contacto + texto)

  envia_mensaje (contacto,texto)


