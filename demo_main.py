# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 13:47:24 2018

@author: liubinghong
"""
import demo_2

from  selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = "http://10.19.2.23:8080/acme/login.html"
driver.get(url)


driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("test2")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("username").submit()
time.sleep(3)

demo_2.login(driver)
#demo_2.logout(driver)