from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.locators.pipeline_creation_locators import PipelineCreationLocator


class PipelineCreationPage:

    def __init__(self, driver):
        self.driver = driver

    def create(self, name: str):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.NAME_INPUT))
        self.driver.find_element(*PipelineCreationLocator.NAME_INPUT).send_keys(name)
        self.driver.find_element(*PipelineCreationLocator.NEXT_BUTTON).click()
        return self

