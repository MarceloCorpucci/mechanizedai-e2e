from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from core.locators.pipeline_overview_locators import PipelineOverviewLocator


class MantineSelectHelper:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
        self.select = None

    def on_component(self, mantine_input_select: WebElement):
        self.select = mantine_input_select
        return self

    def expand(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(PipelineOverviewLocator.SELECT_AN_APP))
        self.select.click()
        return self

    def select_active_descendant(self):
        self.action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        return self

    def select_app(self, app_name):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineOverviewLocator.AVAILABLE_APPS))
        available_apps = self.driver.find_elements(*PipelineOverviewLocator.AVAILABLE_APPS)
        for app in available_apps:
            if app.text == app_name:
                app.click()
                break
        return self

    def return_value_attribute_from_active_descendant(self) -> str:
        self.return_value_attribute_from_active_descendant()
        WebDriverWait(self.driver, 15).until(
            EC.element_attribute_to_include(PipelineOverviewLocator.SELECT_AN_APP, 'value'))
        return self.select.get_attribute('value')