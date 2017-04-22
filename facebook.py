#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:35:14 2017

@author: ska

Auto Login Facebook
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass


print("Enter Username of your TCS CampusCommune")
uname = input()
passw = getpass.getpass()


driver= webdriver.Firefox()

driver.get("https://www.facebook.com")
#time.sleep(5)
username = driver.find_element_by_id("email")
passwd = driver.find_element_by_id("pass")
username.send_keys(uname)
passwd.send_keys(passw)
#driver.find_elements_by_class_name("uiButton").click()
signin=driver.find_element_by_id("u_0_q")
signin.click()
time.sleep(10)