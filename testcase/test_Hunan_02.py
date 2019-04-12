# coding:utf-8
"""
统计分析-车辆安装数
"""
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Hunan_pages
import sys
import time
from config import datas_path
from common.get_parameter import Data

data = Data(datas_path + "Hunan_datas.xlsx", "Sheet1")
param = data.get_data()


class Hunan_Statistic_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global logger
        global driver
        logger = Log()
        # 实例化浏览器引擎
        logger.info('############################### START ###############################')
        driver = Browser_engine().get_browser()
        # driver = Browser_engine().get_browser()
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.max_window()
        cls.index.open_Hunan(param[1]["url"])
        cls.index.username_input(param[1]["username"])
        cls.index.password_input(param[1]["password"])
        cls.index.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    def test_001_CarStatistic(self):
        logger.info("开始用例： {0}".format(sys._getframe().f_code.co_name))
        self.index = Hunan_pages.Hunan_pages_Statistic(driver)
        self.index.F5()
        self.index.statistic_bt_click()
        self.index.installareadata_area_input(param[5]["area"])
        self.index.installareadata_btime_input(param[5]["btime"])
        self.index.sleep(2)
        self.index.installareadata_etime_input(param[5]["etime"])
        self.index.installareadata_cartype_click()
        self.index.installareadata_cartype_check(param[5]["cartype1"])
        self.index.installareadata_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )