from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.selenium.dev/")
print(driver.title)
time.sleep(3)

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
time.sleep(3)

driver.back()
print(driver.title)
time.sleep(3)

driver.forward()
print(driver.title)
driver.quit()

