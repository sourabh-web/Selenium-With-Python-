import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://www.google.com/")
        titleOfPage=driver.title
        #assertEqual
        #self.assertEqual("Google123",titleOfPage,"webpage title are not same")
        self.assertNotEqual("Google",titleOfPage)

if __name__=="__main__":
    unittest.main()
