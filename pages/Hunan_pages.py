# coding:utf-8
from common.basepage import pyselenium

from config import datas_path



class Hunan_pages_login(pyselenium):
    """登录"""

    def open_Hunan(self,URL):

        self.open(URL)

    def type_username(self,username):
        self.type("css->#txtUser", username)

    def type_password(self,password):

        self.type("css->#txtPwd", password)

    def click_login(self):
        self.click("css->.login-btn")


class Hunan_pages_Synch(pyselenium):
    """基本信息车辆管理"""

    def move_to_settings(self):
        self.move_to_element("css->#home-down-icon-level")

    def basicinformation_click(self):
        self.click("css->#base_info_level")

    # def type_carNums(self):
    #     for i in range(5):
    #         carNUM = para[i]["carNUM"]
    #         self.type("css->#vehicleManage_tables_div_queyFrom0_form0_text0_show", carNUM)
    #         i += 1

    def carNum_type(self,car_numeber):
        self.type("css->#vehicleManage_tables_div_queyFrom0_form0_text0_show", car_numeber)

    def select_bt_click(self):
        self.click("css->#vehicleManage_tables_div_queyFrom0_form1_button0_btn")

    def carinfo_click(self):
        self.click("css->#vehicleManage_tables_table > tbody > tr:nth-child(1)")

    def synch_bt_click_(self):
        self.click("css->#vehicleManage_tables_div_queyFrom0_form1_button1_btn")

    def synch_YES_click(self):
        self.click("css->#layui-layer5 > div.layui-layer-btn > a.layui-layer-btn0")
