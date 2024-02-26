from selenium.webdriver.common.by import By


class PipelineCreationLocator:
    NAME_INPUT = (By.XPATH, '//input[@input="name"]')
    NEXT_BUTTON = (By.XPATH, '//*[@id="btn-create-job"]')
