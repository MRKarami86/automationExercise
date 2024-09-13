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

        self.LoginPage.login("mr.karami86@gmail.com", "123456")

        try:
            loginUser = self.driver.find_element(By.XPATH, "//i[@class='fa fa-user']/following-sibling::b[1]")
            loginUserText = loginUser.text
            userName = "MRKarami86"
            assert loginUserText == userName
            print(f"Verify that 'Logged in as {userName}' is visible")
        except AssertionError:
            print(f"AssertionError: expected 'Logged in as {userName}'")

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
        try:
            signupForm = self.driver.find_element(By.XPATH, "//div[@class='login-form']//h2[1]")
            signupFormTest = signupForm.text
            assert signupFormTest == "Login to your account"
            print("Verify that user is navigated to login page")
        except AssertionError:
            print("AssertionError: expected 'Verify that user is navigated to login page'")


if __name__ == "__main__":
    unittest.TestCase()
