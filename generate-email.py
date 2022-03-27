from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
#https://www.randomlists.com/email-addresses?qty=12

def generateEmails():

  qty = input("How many emails do you need  generated?: ")

  url = ("https://www.randomlists.com/email-addresses?qty=" + qty)

  print(url)

  

generateEmails()
