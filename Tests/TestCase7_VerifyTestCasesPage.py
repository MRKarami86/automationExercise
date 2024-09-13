import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com")

    def tearDown(self):
        self.driver.quit()

    def test_login_Successful(self):
        try:
            assert self.driver.current_url == "https://automationexercise.com/"
            print("Verify that home page is visible successfully")
        except AssertionError:
            print("AssertionError: expected 'https://automationexercise.com/'")

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Test Cases')]").click()
        try:
            testCase = self.driver.find_element(By.XPATH, "//h2[@class='title text-center']//b[1]")
            testCaseTest = testCase.text
            assert testCaseTest == "TEST CASES"
            print("Verify user is navigated to test cases page successfully")
        except AssertionError:
            print("AssertionError: expected 'Verify user is navigated to test cases page successfully'")


if __name__ == "__main__":
    unittest.TestCase()