from selenium.webdriver.common.by import By


class HomeLocator:
    WELCOME_LABEL = (By.XPATH, '//h1[contains(@class, "mantine-Text-root")]')
    VIEW_INSIGHT_BUTTON = (By.XPATH, '//*[text()="Insights"]')