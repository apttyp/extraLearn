#coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(level=logging.DEBUG)

options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options = options)
driver.get('http://t.dui.ai/')
time.sleep(2)
# driver.maximize_window()
print driver.title
print driver.current_window_handle
time.sleep(2)
driver.find_element_by_xpath('//*[@id="btn-login"]').click()

driver.find_element_by_xpath('//*[@id="account"]').send_keys('tonystark@aispeech.com')
driver.find_element_by_xpath('//*[@id="pw"]').send_keys('Admin@123')

driver.find_element_by_xpath('//*[@id="form"]/span').click()


#driver.find_element('//*[@id="btn-login"]').click()
#js='window.open("https://www.sogou.com");'
#driver.execute_script(js)
#print driver.current_window_handle 
