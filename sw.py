# -*- coding:utf-8 -*-
from selenium import webdriver
import time

def start_webdriver(name):
    try:
        if (name=='chrome') or (name=='Chrome'):
            print("Start ChromeWebdriver now!")
            driver = webdriver.Chrome()
            return driver
        else:
            pass
    except Exception as msg:
        print('start webdriverError,Error_message:"%s"'%str(msg))
        # driver.quit()

if __name__=="__main__":
    name = 'Chrome'
    start_webdriver(name)

