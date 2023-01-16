#! /usr/bin/python3
#--------------------------------------------------------------------------------------------------------------
  
  
  
  #DEependencies
  #---> pip3 install os
  #---> install any web driver(in this case firefox's geckodriver)



  #------------------------------------------------------------------------------------------------------------


import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()  #calling the firefox driver  (installed from gitub)



browser.get('http://192.168.1.1:8090/') #opens the browser and also open the given link

username = browser.find_element(By.NAME, 'username')  #giving the css_selector path of the username text box(or where user needs to provide input)
password = browser.find_element(By.NAME, 'password')  # css_selector path of the password
username.send_keys("Test")  #this will type the username and password
password.send_keys("Hero@8055")
#login_button = browser.find_element_by_xpath('//*[@id="loginbutton"]')
login_button = browser.find_element(By.XPATH, '//*[@id="loginbutton"]')   #giving the xpath of the login button
login_button.click()									#clicks the login button
browser.close()     #closes the browser
speak="\"connected to Alvas Internet\""
cmd = "{0} {1}".format("espeak ", speak)   #sudo apt install espeak(works only on linux machines)
os.system(cmd)

#browser=webdriver.Firefox()							#can open the browser for another session							
#browser.get('https://www.youtube.com/')

#Author-Nagarjuna GS
