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
#url="
# git
#
#url=https://www.google.com/search?q=git&sxsrf=AJOqlzWvXx5s-eUke_djiK8uwW9VHiwunQ%3A1674148064706&source=hp&ei=4HjJY8j6KNCiseMPjeGl2Ag&iflsig=AK50M_UAAAAAY8mG8L9LAK8y74zp2fHhsF77HMDyZ9qF&ved=0ahUKEwjI6sjFj9T8AhVQUWwGHY1wCYsQ4dUDCAg&uact=5&oq=git&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyEQguELEDEIMBEMcBENEDEJECMgQIABBDMgQIABBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgQIABBDOgcIIxDqAhAnOhAILhCxAxCDARDHARDRAxBDOgUIABCRAjoHCAAQsQMQQ1DQClitDWDDDmgBcAB4AIABfogB7wKSAQMwLjOYAQCgAQGwAQo&sclient=gws-wiz
url=input("enter the url:")
kkey=""

if len(url)==0:
  keyword=input("Enter your query:")
  if len(keyword)!= 0 :
    keylist=list(keyword.split(" "))
    for x in keylist:
      kkey += x
    url="https://www.google.com/search?q=" + kkey +"&sxsrf=AJOqlzWvXx5s-eUke_djiK8uwW9VHiwunQ%3A1674148064706&source=hp&ei=4HjJY8j6KNCiseMPjeGl2Ag&iflsig=AK50M_UAAAAAY8mG8L9LAK8y74zp2fHhsF77HMDyZ9qF&ved=0ahUKEwjI6sjFj9T8AhVQUWwGHY1wCYsQ4dUDCAg&uact=5&oq=git&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyEQguELEDEIMBEMcBENEDEJECMgQIABBDMgQIABBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgQIABBDOgcIIxDqAhAnOhAILhCxAxCDARDHARDRAxBDOgUIABCRAjoHCAAQsQMQQ1DQClitDWDDDmgBcAB4AIABfogB7wKSAQMwLjOYAQCgAQGwAQo&sclient=gws-wiz"

browser = webdriver.Firefox()  #calling the firefox driver  (installed from gitub)



browser.get('http://192.168.1.1:8090/') #opens the browser and also open the given link

username = browser.find_element(By.NAME, 'username')  #giving the css_selector path of the username text box(or where user needs to provide input)
password = browser.find_element(By.NAME, 'password')  # css_selector path of the password
username.send_keys("4al20ec027")  #this will type the username and password
password.send_keys("Newpassword3#")
#login_button = browser.find_element_by_xpath('//*[@id="loginbutton"]')
login_button = browser.find_element(By.XPATH, '//*[@id="loginbutton"]')
#giving the xpath if the login button
login_button.click()									#clicks the login button
browser.close()     #closes the browser
speak ="Connected to Alvas internet"
cmd = "{0} {1}".format("espeak ", speak)# (sudo apt install qrencode)
os.system(cmd)

if len(url)>0:
  browser=webdriver.Firefox()							#can open the browser for another session							
  browser.get(url)

#Author-Nagarjuna GS
