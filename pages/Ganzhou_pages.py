# coding:utf-8
from common.basepage import pyselenium



class Ganzhou_pages_login(pyselenium):
    """登录"""
    def open_Ganzhou(self,URL):
        self.open(URL)

    def type_username(self,username):
        self.type("css->#txtUser", username)

    def type_password(self,password):
        self.type("css->#txtPwd", password)

    def click_login(self):
        self.click("css->#btnLogin")

class Ganzhou_pages_Tongjifenxi(pyselenium):
    """统计分析"""
    def click_tongji(self):
        self.click("css->.home-content-function-blocks-staticAnalys.page-load")
