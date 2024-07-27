import time
import pytest
import unittest
import sys
import os

from POM.ProductPage import ProductPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.MainMenuPage import MainMenuPage


class TestVerifyElementsAreSortedByAsc(BaseClass):

    def test_VerifyElementsAreSortedByAscOrder(self):
        log = self.get_Logger()
        driver = self.driver
        log.info("Se abre la home page")
        hp = HomePage(driver)
        hp.closeModal()
        log.info("Se cierra el primer modal")
        mp = MainMenuPage(driver)
        mp.selectHighLightCafe()
        log.info("Se selecciona la opción High Ligh Cafe")
        hp.closeModal()
        log.info("Se cierra el segundo modal")
        pp = ProductPage(driver)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,700)")
        log.info("Hago scroll hasta la mitad de la pantalla para visualizar el dropdown")
        time.sleep(2)
        orderListExpected = ['Aperol Spritz 200ml', 'Aviation American Gin 50ml', 'Bacon Stone Baked Roll',
                     'Bistrot Chic Merlot 187ml', 'Black Cow Vodka 50ml', 'Brewdog Speedbird OG IPA 330ml',
                     'Brewdog Wingman Session IPA 330ml', 'Brewgooder Fair Trade IPA 330ml',
                     'Cadbury Dairy Milk Chocolate Bar 45g']
        log.info("Click en Sort By, ordenando la lista de la A-Z")
        pp.selectSortByDropdown()
        orderByAsc = "Product A-Z"
        pp.selectItemFromDropDrown(orderByAsc)
        time.sleep(4)
        log.info("Almaceno la lista ordenada alfabéticamente de la A a la Z")
        orderListActualSortedByAZ = pp.showAllElementsNotSortedBySomeOrder()
        time.sleep(3)
        log.info("Y ejecuto un assert para verificar que la lista que obtuve y la que tengo como esperada son iguales, de la primera página de índice")
        assert orderListActualSortedByAZ == orderListExpected
        time.sleep(2)






