from core.locators.insight_locators import InsightLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.pages.pipeline_overview_page import PipelineOverviewPage


class InsightPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_pipelines(self) -> PipelineOverviewPage:
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(InsightLocator.PIPELINE_BUTTON))
        self.driver.find_element(*InsightLocator.PIPELINE_BUTTON).click()
        return PipelineOverviewPage(self.driver)

