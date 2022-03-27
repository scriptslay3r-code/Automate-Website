from selenium import webdriver

#https://www.randomlists.com/email-addresses?qty=12

def generateEmails():

  qty = input("How many emails do you need  generated?: ")

  url = ("https://www.randomlists.com/email-addresses?qty=" + qty)

  print(url)

  

generateEmails()
