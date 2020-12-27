from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
driver.implicitly_wait(10)
assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("submit").click()