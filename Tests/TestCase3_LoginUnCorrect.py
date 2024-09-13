import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com")
        self.LoginPage = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_Successful(self):
        try:
            assert self.driver.current_url == "https://automationexercise.com/"
            print("Verify that home page is visible successfully")
        except AssertionError:
            print("AssertionError: expected 'https://automationexercise.com/'")

        self.driver.find_element(By.XPATH, "//a[contains(.,'Signup / Login')]").click()
        try:
            signupForm = self.driver.find_element(By.XPATH, "//div[@class='login-form']//h2[1]")
            signupFormTest = signupForm.text
            assert signupFormTest == "Login to your account"
            print("Verify 'Login to your account' is visible")
        except AssertionError:
            print("AssertionError: expected 'Login to your account'")

        self.LoginPage.login("mrkarami86@gmail.com", "1234567")

        try:
            errorLogin = self.driver.find_element(By.XPATH, "//input[@name='password']/following-sibling::p[1]")
            errorLoginText = errorLogin.text
            assert errorLoginText == "Your email or password is incorrect!"
            print("Verify that 'Your email or password is incorrect!' is visible")
        except AssertionError:
            print("AssertionError: expected 'Your email or password is incorrect!'")


if __name__ == "__main__":
    unittest.TestCase()
