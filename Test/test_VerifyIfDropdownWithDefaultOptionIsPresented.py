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


class TestVerifyIfSortByDropdownExist(BaseClass):

    def test_VerifyIfDropdownWithDefaultOptionIsPresented(self):
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
        sortByDropdownElement = pp.verifyIfSortByDropdownExist()
        assert sortByDropdownElement is True
        log.info("realizo un assert para verificar que el componente dropdown Sort By exista")
        valueByDefault = pp.getTitleFromSortByDropdown()
        log.info("Verifico que por defecto el titulo en el dropdown sea Default y realizo un assert")
        assert valueByDefault == "Default"





