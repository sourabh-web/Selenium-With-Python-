from selenium import webdriver
from selenium.webdriver.common.by import By


driver= webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

links = driver.find_element(By.TAG_NAME,"a")

driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a").click()