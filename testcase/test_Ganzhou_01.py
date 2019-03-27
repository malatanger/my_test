# coding:utf-8
import unittest
from common.basepage import Browser_engine
from common.log import Log
from common.basepage import pyselenium
from pages import Ganzhou_pages
import time



class Ganzhou_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global logger
        global driver
        logger = Log()
        #实例化浏览器引擎
        logger.info('############################### START ###############################')
        driver = Browser_engine().get_browser()
        # cls.index = Ganzhou_pages.Ganzhou_pages_login(driver)
        # cls.index.open_Ganzhou()

    @classmethod
    def tearDownClass(cls):
        driver.quit()
        logger.info('################################ End ################################')

    def test_01(self):
        self.index = Ganzhou_pages.Ganzhou_pages_login(driver)
        self.index.open_Ganzhou()
        self.index.take_screenshot()

    def test_02(self):
        self.index = Ganzhou_pages.Ganzhou_pages_login(driver)
        self.index.type_username()
        self.index.take_screenshot()
        self.index.type_password()
        self.index.take_screenshot()

