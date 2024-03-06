from selenium.webdriver.common.by import By


class PipelineOverviewLocator:
    OVERVIEW_LABEL = (By.XPATH, '//*[text()="Pipelines Overview"]')
    SELECT_AN_APP = (By.XPATH, '//input[@type="search"]')
    AVAILABLE_APPS = (By.XPATH, '//*[@role="option"]')
    CREATE_BUTTON = (By.XPATH, '//*[@id="add-job-button"]')
