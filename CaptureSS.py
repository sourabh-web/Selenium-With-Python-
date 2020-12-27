from selenium import webdriver


driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

#driver.save_screenshot("C:\\Downloadfiles\\homepage.png")

driver.get_screenshot_as_file("C:\\Downloadfiles\\homepage1.jpg")