# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:43:20 2018

@author: liubinghong
"""

from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
#打开上传功能页面
file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)
#定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')

time.sleep(3)
driver.quit()