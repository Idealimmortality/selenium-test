# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 15:41:29 2018

@author: liubinghong
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = "https://www.baidu.com/"
driver.get(url)

#先去定位设置按钮

Set_button= driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(Set_button).perform()

#定位搜索设置和保存设置按钮

driver.find_element_by_class_name("setpref").click()
time.sleep(1)s
driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo').click()

#定位alert弹出框,使用 
alert = driver.switch_to_alert()
print(alert.text)
alert.accept()
                                 
time.sleep(1)
driver.quit()