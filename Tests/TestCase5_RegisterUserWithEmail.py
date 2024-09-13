import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.SignUpPage import SignUpPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com")
        self.SignUpPage = SignUpPage(self.driver)

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

        self.SignUpPage.SignUp("MRKarami86", "mr.karami86@gmail.com")

        try:
            emailUserError = self.driver.find_element(By.XPATH, "(//input[@type='hidden']/following-sibling::p)[1]")
            emailUserErrorText = emailUserError.text
            assert emailUserErrorText == "Email Address already exist!"
            print("Verify error 'Email Address already exist!' is visible")
        except AssertionError:
            print(f"AssertionError: expected 'Verify error 'Email Address already exist!' is visible'")


if __name__ == "__main__":
    unittest.TestCase()
