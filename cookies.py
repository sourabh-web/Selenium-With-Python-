from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.amazon.in/")

cookies=driver.get_cookies()
print(len(cookies))

print(cookies)
#adding new cookies to the browser

cookie={'name':'Mycookie', 'value':'1234567890'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#deleting cookies
driver.delete_cookie('Mycookie')
cookies=driver.get_cookies()
print(len(cookies))

print(cookies)

