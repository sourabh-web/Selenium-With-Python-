from selenium import webdriver
import time


driver= webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)
time.sleep(1)







