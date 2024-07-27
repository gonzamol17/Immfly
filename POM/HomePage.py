import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePageLocators:
    closeModal = (By.ID, "close-modal")


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def closeModal(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "close-modal")))
        element.click()






