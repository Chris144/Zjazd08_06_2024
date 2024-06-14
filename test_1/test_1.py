import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBase:
    """
    Base class for each test
    """

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        # Setup Phase
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/")
        self.driver.implicitly_wait(5)
        request.cls.driver = self.driver
        # Yield to test
        yield
        # Teardown Phase
        self.driver.quit()

    def test_check_text(self):
        text = self.driver.find_element(By.CLASS_NAME, 'sek-module-inner')
        assert text.text == "Design your own space"
        print(text.text)


if __name__ == '__main__':
    pytest.main()
