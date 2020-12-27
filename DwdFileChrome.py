from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",("download.default_directory": "C:\\Downloadfiles"))



driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe",chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("testing dwd text file")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()


driver.find_element_by_id("pdfbox").send_keys("testing dwd pdf file")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()


