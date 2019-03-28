# coding:utf-8
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Hunan_pages
import time

class Hunan_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global logger
        global driver
        logger = Log()
        # 实例化浏览器引擎
        logger.info('############################### START ###############################')
        driver = Browser_engine().get_browser()
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.open_Hunan()
        cls.index.type_username()
        cls.index.type_password()
        cls.index.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    def test_Synch(self):
        self.index = Hunan_pages.Hunan_pages_Synch(driver)
        self.index.move_to_settings()
        time.sleep(2)
        self.index.click_basicinformation()
        time.sleep(1)
        self.index.type_carNum()
        time.sleep(1)