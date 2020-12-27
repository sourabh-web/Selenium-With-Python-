from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element_by_class_name("uitk-tab-text").click()

time.sleep(2)