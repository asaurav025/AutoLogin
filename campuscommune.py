#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:12:38 2017

@author: ska

AutoLogin TCS Campus Commune everyday from the time of first execution
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import getpass


def login(uname, passw):
	driver= webdriver.Firefox()
	
	driver.get("https://campuscommune.tcs.com/en-in/intro")
	username = driver.find_element_by_id("user_name")
	passwd = driver.find_element_by_id("user_password")
	username.send_keys(uname)
	
	passwd.send_keys(passw,Keys.ENTER)
	print("Username and Password Entered")
	
#signin=driver.find_element_by_type("submit")
#driver.find_element_by_id("loginform").submit()
print("Enter Username of your TCS CampusCommune")
uname = input()
passw = getpass.getpass()


#==============================================================================
# uname = "*****@gmail.com"
# passw = "000000"
#==============================================================================
time.sleep(10)
while True:
	login(uname, passw)
	time.sleep(60*60*24)
