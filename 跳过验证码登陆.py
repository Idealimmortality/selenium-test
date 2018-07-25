#coding=utf-8
from selenium import webdriver
import time,requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://passport.cnblogs.com/user/signin")
# driver.find_element_by_link_text(u"登录").click()
#添加抓到的cookies
driver.add_cookie({'name':".CNBlogsCookie",'value':'DFF47BE141DBE839ACC0E1EF49EE58944777C5A075195946926253FCFCBF69B2F18F3C4595E16E2D607097CFAF8BD46D43D62023B5D51DF24D931D675A73CB1561DA238278B41EEBBFAF184E61A13CA6E8A1EE1E'})

driver.add_cookie({'name':".Cnblogs.AspNetCore.Cookies",'value':'CfDJ8FHXRRtkJWRFtU30nh_M9mBhtsdTitKMZyGpwaUhyuhufZSQ7nhc8SEgBWzjeS8XKXuhOQMY6t_r13CTaAem7hryrVOrb3pXY9da4qBicH74wBrQ70SDntn2hXQRENGI--RFkB-2zJPkUGnGjG1v6TN83N7dwcJxYzcDTMeAYH34kA7PHBqqTwT2frMXvx0EoKIC_f6ttqK8s8ViyQABFtO_Qdwk8cexwt1z_4xcpucb8I6l-x9eP5NUf8IdO2ELbmsR7MirDpETrJyzjFNObqIGsRy3q-0TM0ZCCrx6JdIVsuasK5qV9S65QjQEdebi4w'})

#注意：重新get的地址需要是登陆成功后的地址，不能刷新或者进入以前的地址，否则登陆不进去。

driver.get("https://www.cnblogs.com/cate/2/")
# ActionChains(driver).send_keys(Keys.F5)
time.sleep(3)
aa = driver.find_element_by_xpath("//*[@id='span_userinfo']/a[1]").text
print(aa)
driver.quit()