import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from art import *

welcome = text2art("Welcome")

going = text2art("Going")

headless = text2art("Headless!")

opening = text2art("Opening")

browser = text2art("Browser!")


url =("https://limewire.com/invite/668f67358badde5e6de7")

#emailList = open(emailList.txt, 'r')

answer = input("Headless? [Y] for Yes: ")

if answer == 'y':
  options = Options()
  
  options.add_argument('--headless')
  
  options.add_argument('--disable-gpu')

  print(welcome)

  time.sleep(.5)

  print(going)

  time.sleep(.5)

  print(headless)

  time.sleep(.5)

  ''' 
  # using this filepath is optional and for linux.
  driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
  '''
  driver = webdriver.Chrome(Options=options)
  with open("emailList.txt") as emailList:

    for line in emailList:

        

        driver.get(url); time.sleep(1) #Delay a second  let page load make seem more human maybe

        email_box = driver.find_element_by_name('waitlist[email]')

        email_box.send_keys(line)

        email_box.submit(); time.sleep(1)
        ### The use of Semicolon in python is as the line terminator where it is used as a separator to separate multiple lines. ###
        driver.quit()

# i 
else:

  driver = webdriver.Chrome('/usr/local/bin/chromedriver')

  print(welcome)

  time.sleep(.5)

  print(opening)

  time.sleep(.5)

  print(browser)

  time.sleep(.5)
  with open("emailList.txt") as emailList:

    for line in emailList:

        #print(item)

        

        driver.get(url); time.sleep(3) # Let the user actually see something! 

        email_box = driver.find_element_by_name('waitlist[email]')

        email_box.send_keys(line)

        email_box.submit() 

        time.sleep(3) # Let the user actually see something!

        driver.quit()



