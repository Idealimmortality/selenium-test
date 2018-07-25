# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:09:52 2018
隐式等待就是 设置一个固定的时间，在这段时间内，程序不断的去执行获取想要的元素；隐式等待只需要设置
一次就行了；
@author: liubinghong
"""

from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10) #设置implictly_wait的大小，就可以调整隐式等待的时间；
driver.get('https://www.baidu.com')

input_ = driver.find_element_by_id("kw22")
input_.send_keys("selenium")

driver.quit()