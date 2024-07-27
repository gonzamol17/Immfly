from selenium.webdriver.common.by import By


class MainMenuLocators:
    highLightCafeOption = (By.XPATH, " //a[contains(text(),'HIGH LIFE CAFÉ ')]")


class MainMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def selectHighLightCafe(self):
        self.driver.find_element(*MainMenuLocators.highLightCafeOption).click()






