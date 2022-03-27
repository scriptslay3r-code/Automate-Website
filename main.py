import time

from selenium import webdriver

###### Version 0.1 #####
#### OLD ####



url =("https://limewire.com/invite/668f67358badde5e6de7")

driver = webdriver.Chrome('/usr/local/bin/chromedriver')


driver.get(url)

time.sleep(3) 

email_box = driver.find_element_by_name('waitlist[email]')

email_box.send_keys("mysignupemail@gmail.com")

email_box.submit() 

time.sleep(3) 

driver.quit()



