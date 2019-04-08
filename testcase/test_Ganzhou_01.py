# coding:utf-8
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Ganzhou_pages
from common.get_parameter import Data
from config import datas_path
import time

data = Data(datas_path + "Ganzhou_datas.xlsx", "Sheet1")
param = data.get_data()


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
        cls.index.max_window()
        cls.index.open_Ganzhou(param[2]["url"])
        cls.index.type_username(param[2]["username"])
        cls.index.type_password(param[2]["password"])
        cls.index.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.index = Ganzhou_pages.Ganzhou_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    def test_01(self):
        self.index = Ganzhou_pages.Ganzhou_pages_Statistics(driver)
        self.index.click_Statistics()
