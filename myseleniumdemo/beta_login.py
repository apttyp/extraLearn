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
driver.get('https://www.baidu.com')
time.sleep(2)
print driver.find_element_by_xpath('//*[@id="lg"]')
driver.maximize_window
print driver.title
print driver.current_window_handle
time.sleep(2)
js='window.open("https://www.sogou.com");'
driver.execute_script(js)
print driver.current_window_handle 

handles = driver.window_handles 
print handles 

for handle in handles:
    if handle!=driver.current_window_handle:
        print 'switch to ',handle
        driver.switch_to_window(handle)
        print driver.current_window_handle 
        break
