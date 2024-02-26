from selenium.webdriver.common.by import By


class LoginLocator:
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    CONTINUE_BUTTON = (By.ID, 'login-button')
