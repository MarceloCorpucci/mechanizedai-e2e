from core.locators.home_locators import HomeLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.pages.insight_page import InsightPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def is_welcome_message_present(self) -> bool:
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(HomeLocator.WELCOME_LABEL))
        return self.driver.find_element(*HomeLocator.WELCOME_LABEL).is_displayed()

    def go_to_mechanized_insights(self) -> InsightPage:
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(HomeLocator.VIEW_INSIGHT_BUTTON))
        self.driver.find_element(*HomeLocator.VIEW_INSIGHT_BUTTON).click()
        return InsightPage(self.driver)
