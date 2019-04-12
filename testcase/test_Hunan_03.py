# coding:utf-8
"""
基本信息-车辆信息
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


class Hunan_assessment_test(unittest.TestCase):

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
        cls.index.open_Hunan(param[6]["url"])
        cls.index.username_input(param[6]["username"])
        cls.index.password_input(param[6]["password"])
        cls.index.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    def test_001_Areaassessment_mouth(self):
        logger.info("开始用例： {0}".format(sys._getframe().f_code.co_name))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.areaassessment_type_choose(param[6]["assessmenttype"])
        self.index.areaassessment_area_input(param[6]["area"])
        self.index.areaassessment_mouth_time_input(param[6]["btime"])
        self.index.areaassessment_cartype_click()
        self.index.areaassessment_cartype_check(param[6]["cartype1"])
        self.index.areaassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )

    def test_002_Areaassessment_year(self):
        logger.info("开始用例： {0}".format(sys._getframe().f_code.co_name))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.areaassessment_type_choose(param[7]["assessmenttype"])
        self.index.sleep(3)
        self.index.areaassessment_area_input(param[7]["area"])
        self.index.areaassessment_year_time_input(param[7]["btime"])
        self.index.areaassessment_cartype_click()
        self.index.areaassessment_cartype_check(param[7]["cartype1"])
        self.index.areaassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr",
            #sec=20
        )

    def test_003_Areaassessment_day(self):
        logger.info("开始用例： {0}".format(sys._getframe().f_code.co_name))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.areaassessment_type_choose(param[8]["assessmenttype"])
        self.index.sleep(3)
        self.index.areaassessment_area_input(param[8]["area"])
        self.index.areaassessment_btime_input(param[8]["btime"])
        self.index.areaassessment_etime_input(param[8]["etime"])
        self.index.areaassessment_cartype_click()
        self.index.areaassessment_cartype_check(param[8]["cartype1"])
        self.index.areaassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )
