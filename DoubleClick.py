from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

ele=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions=ActionChains(driver)

actions.double_click(ele).perform()