# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 14:12:33 2018

@author: liubinghong
"""
import time
from selenium import webdriver
driver = webdriver.Chrome()
url = "http://11.24.201.130/acme/index.html"
driver.implicitly_wait(10)
driver.get(url)
try:
    driver.find_element_by_id("username").send_keys("23432348")
    driver.find_element_by_id("password").send_keys("admin123")
    driver.find_element_by_id("username").submit()
    time.sleep(3)
    
    aa = driver.find_element_by_xpath("//*[@id='loginUserName' and @class='userName']").is_displayed()
#    temp = driver.execute_script("document.getElementById('loginUserName').innerHTML")
    bb = driver.find_element_by_xpath("//*[@id='loginUserName' and @class='userName']").get_attribute("textContent")
    '''
    划重点：如果某个文本内容获取不到，那么首先看看是不是定位的元素被隐藏了，用is_displayed方法
    如果是false，可以用get_attribute（attributeName）
    textContent, innerText, innerHTML等属性获取
    
    innerHTML 会返回元素的内部 HTML， 包含所有的HTML标签。 
    例如，<div>Hello <p>World!</p></div>的innerHTML会得到Hello <p>World!</p>
    textContent 和 innerText 只会得到文本内容，而不会包含 HTML 标签。 
    textContent 是 W3C 兼容的文字内容属性，但是 IE 不支持
    innerText 不是 W3C DOM 的指定内容，FireFox不支持
    
    
    https://www.cnblogs.com/ppppying/p/7755064.html
    '''
    print(bb)
    print(type(aa))
    
except Exception as e :
    print(e)
finally:
    time.sleep(3)
    driver.quit()

