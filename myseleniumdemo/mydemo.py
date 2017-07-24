# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import logging

logging.basicConfig(level=logging.DEBUG)


browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://www.google.com") # Load page
browser.maximize_window()
time.sleep(2)
print browser.title
browser.close()

#browser1 = webdriver.Chrome()
#browser1.get("http://www.baidu.com")
#print browser1.title
#browser1.close()
