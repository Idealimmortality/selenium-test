# -*- coding:utf-8 -*-
from selenium import webdriver
import sw
import time

'''
get_cookies() 获得所有cookie 信息
get_cookie(name) 返回有特定name 值有cookie 信息
get_cookie(name) 返回有特定name 值有cookie 信息
delete_cookie(name) 删除特定(部分)的cookie 信息
delete_all_cookies() 删除所有cookie 信息
'''

#下面的代码主要是循环存放截图的；cookies的操作很简单，根据上面的注释即可完成；

name = 0
def bar():
    global name
    name +=1
    return name

def foo(name):
    try:
        driver = sw.start_webdriver('chrome')
        driver.get("http://www.baidu.com")
        driver.add_cookie({'name':'test','value':'12'})
        cookies = driver.get_cookies()
        driver.find_element_by_class_name('test')
    except Exception as msg:
        driver.get_screenshot_as_file("D:\\TestFile\\"+str(name)+".png")
        driver.get_screenshot_as_png()
        driver.quit()
for i in range(0,5):
    foo(bar())

# for cookie in cookies:
#     print("%s --> %s"%(cookie['name'],cookie['value']))

# driver.delete_all_cookies()

# print('cookies',driver.get_cookies())
# time.sleep(3)
# driver.quit()