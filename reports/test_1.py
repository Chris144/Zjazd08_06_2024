import unittest

import allure
import allure_unittest

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.feature("Base Test")
class TestBase(allure_unittest):
    """
    Base class for each test
    """

    def setUp(self):
        # Setup Phase
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/")
        self.driver.implicitly_wait(5)

    @allure.story("Check Text Presence")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_check_text(self):
        with allure.step("Find element with class name 'sek-module-inner"):
            order = self.driver.find_element(By.CLASS_NAME, 'sek-module-inner')
        with allure.step("Verify the text of the element"):
            self.assertEqual("Design your own space", order.text)
        print(order.text)
        allure.attach(self.driver.get_full_page_screenshot_as_png(), name='test', attachment_type=AttachmentType.PNG)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(allure_unittest.result)
