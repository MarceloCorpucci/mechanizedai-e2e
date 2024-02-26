from core.locators.login_locators import LoginLocator
from core.pages.home_page import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_using(self, email: str, password: str) -> HomePage:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginLocator.EMAIL_INPUT))

        self.driver.find_element(*LoginLocator.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*LoginLocator.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginLocator.CONTINUE_BUTTON).click()

        return HomePage(self.driver)
