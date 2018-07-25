# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:27:04 2018

@author: liubinghong
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver import ActionChains #鼠标事件
from selenium.webdriver.common.keys import Keys #键盘事件

url ='http://fanyi.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_css_selector("#baidu_translate_input").send_keys("test")
#driver.find_element_by_css_selector("#baidu_translate_input").submit()
aa = driver.find_element_by_css_selector("#baidu_translate_input").size
bb = driver.find_element_by_css_selector("#baidu_translate_input").text
cc = driver.find_element_by_css_selector("#baidu_translate_input").is_displayed()
print(aa)
print(bb)
context_click =driver.find_element_by_css_selector("#translate-button")
context_click2 =driver.find_element_by_css_selector("#baidu_translate_input")
try:
    ActionChains(driver).context_click(context_click)
    ActionChains(driver).perform()
except Exception as e:
    print(e)
finally:
    time.sleep(5)
    driver.quit()