from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.components.mantine_select_helper import MantineSelectHelper
from core.locators.pipeline_overview_locators import PipelineOverviewLocator
from core.pages.pipeline_creation_page import PipelineCreationPage


class PipelineOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def is_pipeline_page_displayed(self) -> bool:
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineOverviewLocator.OVERVIEW_LABEL))
        return self.driver.find_element(*PipelineOverviewLocator.OVERVIEW_LABEL).is_displayed()

    def select_application(self):
        # TODO: An addition to select an application based on its name is needed
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineOverviewLocator.SELECT_AN_APP))

        select_app_webelement = self.driver.find_element(*PipelineOverviewLocator.SELECT_AN_APP)
        mantine_select = MantineSelectHelper(self.driver)

        mantine_select \
            .on_component(select_app_webelement) \
            .expand() \
            .select_active_descendant()

        return self

    def go_to_create_pipeline_page(self) -> PipelineCreationPage:
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineOverviewLocator.CREATE_BUTTON))
        self.driver.find_element(*PipelineOverviewLocator.CREATE_BUTTON).click()
        return PipelineCreationPage(self.driver)

