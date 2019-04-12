# coding:utf-8
from common.basepage import pyselenium


class Ganzhou_pages_login(pyselenium):
    """登录"""

    def open_Ganzhou(self, URL):
        self.open(URL)

    def type_username(self, username):
        self.type("css->#txtUser", username)

    def type_password(self, password):
        self.type("css->#txtPwd", password)

    def click_login(self):
        self.click("css->#btnLogin")


class Ganzhou_pages_Statistics(pyselenium):
    """统计分析"""

    def click_Statistics(self):
        self.click("css->.home-content-function-blocks-staticAnalys.page-load")

    def type_area(self, text):
        self.type("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_text0_show", text)
        self.js("document.querySelector('#ui-id-1').style.display='block'")

