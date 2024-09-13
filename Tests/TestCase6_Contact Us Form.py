import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from Pages.ContactUs import contactUs


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com")
        self.contactUs = contactUs(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_Successful(self):
        try:
            assert self.driver.current_url == "https://automationexercise.com/"
            print("Verify that home page is visible successfully")
        except AssertionError:
            print("AssertionError: expected 'https://automationexercise.com/'")

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Contact us')]").click()
        try:
            signupForm = self.driver.find_element(By.XPATH, "//div[@class='contact-form']//h2[1]")
            signupFormTest = signupForm.text
            assert signupFormTest == "GET IN TOUCH"
            print("Verify 'GET IN TOUCH' is visible")
        except AssertionError:
            print("AssertionError: expected 'Verify 'GET IN TOUCH' is visible'")

        self.contactUs.formContactUs("MRK86", "mrk@gmail.com", "Support", "Can i you help me?")
        Alert(self.driver).accept()
        try:
            sendform = self.driver.find_element(By.XPATH, "//div[contains(@class,'status alert')]")
            sendformText = sendform.text
            assert sendformText == "Success! Your details have been submitted successfully."
            print("Verify success message 'Success! Your details have been submitted successfully.' is visible")
        except AssertionError:
            print("AssertionError: expected 'Verify success message 'Success! Your details have been submitted "
                  "successfully.' is visible' ")

        self.driver.find_element(By.XPATH, "//a[@class='btn btn-success']//span[1]").click()
        try:
            assert self.driver.current_url == "https://automationexercise.com/"
            print("verify that landed to home page successfully")
        except AssertionError:
            print("AssertionError: expected 'verify that landed to home page successfully'")


if __name__ == "__main__":
    unittest.TestCase()