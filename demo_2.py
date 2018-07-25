# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 09:49:46 2018

@author: liubinghong
"""
import time

def login(driver):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("test2")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_id("username").submit()
    time.sleep(3)
    
def logout(driver):
    print(driver.find_element_by_class_name("quit").is_displayed())
#    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/ul/li[2]").click()
    
#    driver.execute_script("")
#    aa= driver.find_element_by_xpath("//*[@id='logOut']").is_displayed()
#    print(aa)                                    
    driver.quit()


#logout()