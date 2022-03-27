from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
#https://www.randomlists.com/email-addresses?qty=12

def generateEmails():

  qty = input("How many emails do you need  generated?: ")

  url = ("https://www.randomlists.com/email-addresses?qty=" + qty)

  driver.get(url); time.sleep(1)
  email_list = driver.find_element_by(By.CLASS_NAME, 'Rand-stage')
  print(email_list)

  

generateEmails()
