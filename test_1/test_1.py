import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """

    def test_setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/")
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

