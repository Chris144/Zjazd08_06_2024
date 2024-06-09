import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """

    def test_setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/")
        self.driver.implicitly_wait(5)
        text = self.driver.find_element(By.CLASS_NAME, 'sek-module-inner')
        self.assertEqual(
            "Design your own space",
            text.text)
        print(text.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
