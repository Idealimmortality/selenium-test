# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:48:53 2018

@author: liubinghong
"""

from selenium import webdriver 
import time,os

driver =webdriver.Chrome()
file_path = "file:///"+ os.path.abspath("frame.html")
driver.get(file_path)

try:
    driver.switch_to_frame("if")
    driver.find_element_by_id("kw").send_keys("test")
    driver.find_element_by_id("su").click()
    time.sleep(3)
    #如果要切换frame表单，需要使用switch_to_default_content()方法返回上级表单
    driver.switch_to_default_content()
    driver.switch_to_frame("else")
    driver.find_element_by_id("kw").send_keys("slect")

    time.sleep(3)
except Exception as e :
    print(e)
finally:
    driver.quit()
