from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.locators.pipeline_creation_locators import PipelineCreationLocator
from core.components.random_string_helper import GenerateRandomString

class PipelineCreationPage:

    def __init__(self, driver):
        self.driver = driver

    def create(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.NAME_INPUT))
        self.driver.find_element(*PipelineCreationLocator.NAME_INPUT).send_keys(f"Test_name_{GenerateRandomString.generateLetters(5)}")
        
        self.driver.find_element(*PipelineCreationLocator.DESCRIPTION_INPUT).send_keys(f"Test_description_{GenerateRandomString.generateLettersAndDigits(10)}")
        
        self.driver.find_element(*PipelineCreationLocator.NEXT_BUTTON).click()
        return self

    def add_an_input(self, input_name):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.ADD_NEW_INPUT_BUTTON))
        self.driver.find_element(*PipelineCreationLocator.ADD_NEW_INPUT_BUTTON).click()
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.NAME_INPUT))
        self.driver.find_element(*PipelineCreationLocator.NAME_INPUT).send_keys(f"Test_{GenerateRandomString.generateLetters(5)}")
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.DATA_SET_SOURCE))
        self.driver.find_element(*PipelineCreationLocator.DATA_SET_SOURCE).click()
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.DATASET_SOURCE_OPTION))
        available_options = self.driver.find_elements(*PipelineCreationLocator.DATASET_SOURCE_OPTION)
        for option in available_options:
            if option.text == input_name:
                option.click()
                break
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.ADD_INPUT_BUTTON))
        self.driver.find_element(*PipelineCreationLocator.ADD_INPUT_BUTTON).click()
        return self
    
    def join_inputs(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.ADDED_INPUTS))
        added_inputs = self.driver.find_elements(*PipelineCreationLocator.ADDED_INPUTS)
        for input in added_inputs:
            input.click()
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.JOIN_BUTTON))
        self.driver.find_element(*PipelineCreationLocator.JOIN_BUTTON).click()
        
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.NAME_INPUT))
        self.driver.find_element(*PipelineCreationLocator.NAME_INPUT).send_keys(f"Test_{GenerateRandomString.generateLetters(5)}")

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.EDIT_JOINS_BUTTON))
        self.driver.find_element(*PipelineCreationLocator.EDIT_JOINS_BUTTON).click()

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.LEFT_DF_INPUT))
        self.driver.find_element(*PipelineCreationLocator.LEFT_DF_INPUT).send_keys(GenerateRandomString.generateLettersAndDigits(3))

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.RIGHT_DF_INPUT))
        self.driver.find_element(*PipelineCreationLocator.RIGHT_DF_INPUT).send_keys(GenerateRandomString.generateLettersAndDigits(3))

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.LEFT_ON_INPUT))
        self.driver.find_element(*PipelineCreationLocator.LEFT_ON_INPUT).send_keys(GenerateRandomString.generateLettersAndDigits(3))

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.RIGHT_ON_INPUT))
        self.driver.find_element(*PipelineCreationLocator.RIGHT_ON_INPUT).send_keys(GenerateRandomString.generateLettersAndDigits(3))

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.SAVE_JOIN_BUTTON))
        self.driver.find_element(*PipelineCreationLocator.SAVE_JOIN_BUTTON).click()

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.ADD_JOIN_BUTTON))
        self.driver.find_element(*PipelineCreationLocator.ADD_JOIN_BUTTON).click()
        
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.JOINED_INPUTS_NODE))
        self.driver.find_element(*PipelineCreationLocator.JOINED_INPUTS_NODE).click()

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.OUTPUT_BUTTON))
        self.driver.find_element(*PipelineCreationLocator.OUTPUT_BUTTON).click()

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.NAME_INPUT))
        self.driver.find_element(*PipelineCreationLocator.NAME_INPUT).send_keys(f"Test_{GenerateRandomString.generateLetters(5)}")

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.DATASET_NAME_INPUT))
        self.driver.find_element(*PipelineCreationLocator.DATASET_NAME_INPUT).send_keys(f"Test_{GenerateRandomString.generateLetters(5)}")

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.ADD_OUTPUT_BUTTON))
        self.driver.find_element(*PipelineCreationLocator.ADD_OUTPUT_BUTTON).click()

        return self
    
    def save_pipeline(self):
        
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PipelineCreationLocator.SAVE_PIPELINE_BUTTON))
        self.driver.find_element(*PipelineCreationLocator.SAVE_PIPELINE_BUTTON).click()
        return self