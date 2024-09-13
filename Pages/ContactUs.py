from Locators.Locators import Locators

class contactUs():
    def __init__(self, driver):
        self.driver = driver
        self.Locators = Locators()

    def formContactUs(self, name, Email, Subject, Message):
        self.driver.find_element(*self.Locators.nameContactUs).send_keys(name)
        self.driver.find_element(*self.Locators.emailContactUs).send_keys(Email)
        self.driver.find_element(*self.Locators.subjectContactUs).send_keys(Subject)
        self.driver.find_element(*self.Locators.messageContactUs).send_keys(Message)
        filePathImage = r"D:\1.AutomationTest\Selenium&Python\AutomationExercise\Document\UploadFIle\fileUploadContactUs.png"
        self.driver.find_element(*self.Locators.fileUploadButton).send_keys(filePathImage)
        self.driver.find_element(*self.Locators.submitButton).click()