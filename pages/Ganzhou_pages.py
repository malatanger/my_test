# coding:utf-8
from common.basepage import pyselenium
from common.get_parameter import ExcelUtil
from config import datas_path

data = ExcelUtil(datas_path +"Ganzhou_datas.xlsx" , "Sheet1")
para = data.dict_data()
URL = para[1]["url"]
username = para[1]["username"]
password = para[1]["password"]


class Ganzhou_pages_login(pyselenium):
    """登录"""
    def open_Ganzhou(self):
        self.open(URL)

    def type_username(self):
        self.type("css->#txtUser", username)

    def type_password(self):
        self.type("css->#txtPwd", password)

    def click_login(self):
        self.click("css->#btnLogin")

class Ganzhou_pages_Tongjifenxi(pyselenium):
    """统计分析"""
    def click_tongji(self):
        self.click("css->.home-content-function-blocks-staticAnalys.page-load")



