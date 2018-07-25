# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:22:58 2018

@author: liubinghong
"""
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = "file:///"+os.path.abspath("upfile.html")

driver.get(file_path)

driver.find_element_by_name("file").click()
os.system("C:\\Users\\Administrator\\Desktop\\upfile.exe")
time.sleep(3)
driver.quit()