# coding:utf-8
from common.basepage import pyselenium
from common.get_parameter import ExcelUtil
from config import datas_path

data = ExcelUtil(datas_path +"Hunan_datas.xlsx" , "Sheet1")
para = data.dict_data()
URL = para[0]["url"]
username = para[0]["username"]
password = para[0]["password"]
carNUM = para[0]["carNUM"]

class Hunan_pages_login(pyselenium):
    """登录"""
    def open_Hunan(self):
        self.open(URL)

    def type_username(self):
        self.type("css->#txtUser", username)

    def type_password(self):
        self.type("css->#txtPwd", password)

    def click_login(self):
        self.click("css->.login-btn")

class Hunan_pages_Synch(pyselenium):
    """同步车辆基本信息"""
    def move_to_settings(self):
        self.move_to_element("css->#home-down-icon-level")

    def click_basicinformation(self):
        self.click("css->#base_info_level")

    def type_carNum(self):
        self.type("css->#vehicleManage_tables_div_queyFrom0_form0_text0_show",carNUM)
