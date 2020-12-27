from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver= webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

inputboxes = driver.find_element_by_class_name("text_field")


status=driver.find_element_by_id("RESULT_TextField-1").is_displayed()
print(status)
driver.find_element_by_id("RESULT_TextField-1").is_enabled()
print(status)

driver.find_element_by_id("RESULT_TextField-1").send_keys("sourabh")
driver.find_element_by_id("RESULT_TextField-2").send_keys("hulyalkar")
driver.find_element_by_id("RESULT_TextField-3").send_keys("777777777")