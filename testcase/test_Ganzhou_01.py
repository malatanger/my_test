# coding:utf-8
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Ganzhou_pages
import time

class Ganzhou_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global logger
        global driver
        logger = Log()
        # 实例化浏览器引擎
        logger.info('############################### START ###############################')
        driver = Browser_engine().get_browser()
        cls.index = Ganzhou_pages.Ganzhou_pages_login(driver)
        cls.index.open_Ganzhou()
        cls.index.type_username()
        cls.index.type_password()
        cls.index.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.index = Ganzhou_pages.Ganzhou_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    def test_01(self):
        self.index = Ganzhou_pages.Ganzhou_pages_Tongjifenxi(driver)
        self.index.click_tongji()

