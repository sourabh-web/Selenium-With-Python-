import XLUtils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

path="C:\\Downloadfiles\\Login.xlsx"

row=XLUtils.getRowCount(path, 'Sheet1')

for r in range(2,row+1):
    username=XLUtils.readData(path, "Sheet1",r,1)
    password=XLUtils.readData(path, "Sheet1",r,2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("submit").click()

    if driver.title=="Login: Mercury Tours":
        print("test is passed")
        XLUtils.writeData(path, "Sheet1" ,r,3,"test passed")
    else:
        print("test failed")
        XLUtils.writeData(path, "Sheet1" ,r,3,"test failed")

    driver.find_element_by_link_text("Home").click()


