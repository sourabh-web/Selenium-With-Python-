from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver= webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

time.sleep(2)

driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium.chromium").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_xpath("/html/body/main/ul/li[10]/a").click()
time.sleep(3)
driver.switch_to.default_content()

driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()

