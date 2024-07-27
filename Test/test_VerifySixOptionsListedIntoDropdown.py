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


class TestVerifyIfSixOptionAreVisualized(BaseClass):

    def test_VerifySixOptionsListedIntoDropdown(self):
        log = self.get_Logger()
        driver = self.driver
        log.info("Se está inicializando el browser")
        hp = HomePage(driver)
        hp.closeModal()
        mp = MainMenuPage(driver)
        mp.selectHighLightCafe()
        hp.closeModal()
        pp = ProductPage(driver)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,750)")
        time.sleep(2)
        log.info("Se selecciona el dropdown Sort By")
        pp.selectSortByDropdown()
        value = "Default"
        backgroundcolor = pp.getBackgroundColorFromDropdown(value)
        log.info("Realizo un assert para asegurame que la opción seleccionada por default esté remarcado en fondo con color rojo")
        assert backgroundcolor == "rgba(183, 62, 62, 1)"
        listitemsFromDropdown = ['Default', 'New Arrivals', 'Product A-Z', 'Product Z-A', 'Price Low to High', 'Price High to Low']
        items = pp.getAllElementsFromSortByDropdown()
        aux = pp.verifyEqualsListWithoutOrder(items, listitemsFromDropdown)
        log.info("Realizo un assert para corroborar que al desplegar el dropdown me muestre los 6 elementos")
        assert aux is True
        time.sleep(5)




