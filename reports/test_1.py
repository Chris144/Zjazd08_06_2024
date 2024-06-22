import unittest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.feature("Base Test")
class TestBase(unittest.TestCase):

    @allure.story("Check Text Presence")
    def test_check_text(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http://seleniumdemo.com/")
        driver.implicitly_wait(5)

        try:
            with allure.step("Find element with class name 'sek-module-inner'"):
                order = driver.find_element(By.CLASS_NAME, 'sek-module-inner')
            with allure.step("Verify the text of the element"):
                assert order.text == "Design your own space", f"Expected text 'Design your own space' but got '{order.text}'"
            print(order.text)
        finally:
            driver.quit()

if __name__ == '__main__':
    unittest.main()
