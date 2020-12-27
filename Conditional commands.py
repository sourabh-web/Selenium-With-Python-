from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
time.sleep(5)
ele= driver.find_element_by_name("userName")
print(ele.is_displayed())
print(ele.is_enabled())

pwd= driver.find_element_by_name("password")
print(ele.is_displayed())
print(ele.is_enabled())

ele.send_keys("mercury")
time.sleep(2)
pwd.send_keys("mercury")
time.sleep(2)

driver.find_element_by_name("submit").click()
driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()

r1=driver.find_element_by_css_selector("Input[value=roundtrip]")
print(r1.is_selected())

r2=driver.find_element_by_css_selector("Input[value=oneway]")
print(r2.is_selected())