# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:16:17 2018

@author: liubinghong
"""
"""
使用

"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

url1="https:\\www.baidu.com"
driver.implicitly_wait(10)
driver.get(url1)

#进入百度首页,获取首页句柄
search_handle = driver.current_window_handle
driver.find_element_by_link_text(u"登录").click()
driver.find_element_by_link_text(u"立即注册").click()
#获取所有的句柄
all_handles = driver.window_handles

#现在可以循环遍历all_handles里面的窗口句柄，找到你想要的句柄使用switch_to_window()
#就可以实现切换窗口
for handle in all_handles:
    if handle !=search_handle:
        try:
            driver.switch_to_window(handle)
            print("现在进入到注册窗口")
            driver.find_element_by_name('userName').send_keys("testname")
            driver.find_element_by_name('phone').send_keys("15088888888")
            time.sleep(3)
        except Exception:
            print(Exception)
#        finally:
#            driver.quit()
            
#进入搜索窗口
for handle in all_handles:
    if handle == search_handle:
        driver.switch_to_window(handle)
        driver.find_element_by_class_name("close-btn").click()
        driver.find_element_by_id("kw").send_keys("selenium")
        time.sleep(3)

driver.quit()
        