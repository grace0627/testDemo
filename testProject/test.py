
from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.maximize_window() #窗口最大化

driver.get('https://www.baidu.com') #操控浏览器打印百度主页

time.sleep(10) #暂停10s

print(driver.title)

driver.quit()#退出