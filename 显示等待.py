# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:20:49 2018
显式等待使WebdDriver 等待某个条件成立时继续执行，否则在达到最大时长时抛弃超时异常
@author: liubinghong
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
#expected_conditions 提供了一些预期条件，方便我们调用
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常
#WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
element = WebDriverWait(driver,10,poll_frequency=0.5,ignored_exceptions=Exception).until(
        EC.presence_of_element_located((By.ID,"kw")))
element.send_keys("sb")

driver.quit()

