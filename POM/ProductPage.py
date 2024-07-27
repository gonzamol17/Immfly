from collections import Counter

from selenium.webdriver.common.by import By


class ProductPageLocators:
    sortByDropdown = (By.CSS_SELECTOR, "#layer-product-list > div:nth-child(1) div > ul")
    listFromSortByDropdown = (By.CSS_SELECTOR, "#layer-product-list > div:nth-child(1) > div.toolbar-sorter.sorter  li.options")
    itemsOrderByAsc = (By.CSS_SELECTOR, "a.product-item-link")


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def selectSortByDropdown(self):
        self.driver.find_element(*ProductPageLocators.sortByDropdown).click()

    def verifyIfSortByDropdownExist(self):
        return self.driver.find_element(*ProductPageLocators.sortByDropdown).is_displayed()

    def getTitleFromSortByDropdown(self):
        return self.driver.find_element(*ProductPageLocators.sortByDropdown).text

    def getBackgroundColorFromDropdown(self, value):
        items = self.driver.find_elements(*ProductPageLocators.listFromSortByDropdown)
        for item in items:
            if item.text == value:
                aux = item
                return aux.value_of_css_property('background-color')

            else:
                print("no está la opción buscada")


    def selectItemFromDropDrown(self, value):
        items = self.driver.find_elements(*ProductPageLocators.listFromSortByDropdown)
        for item in items:
            if item.text == value:
                item.click()
                break

    def getAllElementsFromSortByDropdown(self):
        elements = self.driver.find_elements(*ProductPageLocators.listFromSortByDropdown)
        items = []
        for item in elements:
            items.append(item.text)
            #print(item.text)
        return items

    def verifyEqualsListWithoutOrder(self, items, listitemsFromDropdown):
        return Counter(items) == Counter(listitemsFromDropdown)

    def showAllElementsNotSortedBySomeOrder(self):
        elements = self.driver.find_elements(*ProductPageLocators.itemsOrderByAsc)
        lista1 = []
        for ele in elements:
            lista1.append(ele.text)
        return lista1

    def showAllElementSortedBySomeOrder(self):
        elements = self.driver.find_elements(*ProductPageLocators.itemsOrderByAsc)
        lista2 = []
        for ele in elements:
            lista2.append(ele.text)
        return lista2

    def getPrueba(self, lista_sin_ordenar, lis1):
        for i in range(min(len(lista_sin_ordenar), len(lis1))):
            if lista_sin_ordenar[i] != lis1[i]:
                return False
        return len(lista_sin_ordenar) == len(lis1)

