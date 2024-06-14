import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBase(unittest.TestCase):
    """
    Base class for each test
    """

    def setUp(self):
        # Setup Phase
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/")
        self.driver.implicitly_wait(5)

    def test_check_text(self):
        order = self.driver.find_element(By.CLASS_NAME, 'sek-module-inner')
        self.assertEqual("Design your own space", order.text)
        print(order.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
