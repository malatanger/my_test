# coding:utf-8
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Hunan_pages
import time
from config import datas_path
from common.get_parameter import ExcelUtil

data = ExcelUtil(datas_path + "Hunan_datas.xlsx", "Sheet1")
para = data.dict_data()

class Hunan_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global logger
        global driver
        logger = Log()
        # 实例化浏览器引擎
        logger.info('############################### START ###############################')
        driver = Browser_engine().get_browser()
        #driver = Browser_engine().get_browser()
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.max_window()
        cls.index.open_Hunan(para["1"]["url"])
        cls.index.type_username(para[0]["username"])
        cls.index.type_password(para[0]["password"])
        cls.index.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    def test_Synch(self):
        self.index = Hunan_pages.Hunan_pages_Synch(driver)
        self.index.move_to_settings()
        self.index.click_basicinformation()
        self.index.type_carNum(para[0]["carNUM"])
        self.index.click_select_bt()
        self.index.take_screenshot()
        self.index.click_carinfo()
        self.index.click_synch_bt()
        self.index.click_YES()
        try:
            self.index.element_wait("css->.layui-layer-content.layui-layer-padding",sec=15)
            el = self.index.get_text("css->.layui-layer-content.layui-layer-padding")
            self.assertIn("同步成功",el)
        except Exception:
            raise