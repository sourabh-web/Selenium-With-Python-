from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("http://www.google.com")

time.sleep(0.2)

print(driver.title)
print(driver.page_source)
print(driver.close())
