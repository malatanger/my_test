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


class Hunan_pages_BaseInfo(pyselenium):
    """基本信息车辆管理"""

    def move_to_settings(self):
        self.move_to_element("css->#home-down-icon-level")

    def baseinfo_click(self):
        # 点击基本信息
        self.click("css->#base_info_level")

    # def type_carNums(self):
    #     for i in range(5):
    #         carNUM = para[i]["carNUM"]
    #         self.type("css->#vehicleManage_tables_div_queyFrom0_form0_text0_show", carNUM)
    #         i += 1

    def type_carnum(self,car_numeber):
        # 输入车牌号
        self.type("css->#vehicleManage_tables_div_queyFrom0_form0_text0_show", car_numeber)

    def select_bt_click(self):
        # 查询
        self.click("css->#vehicleManage_tables_div_queyFrom0_form1_button0_btn")

    def carinfo_click(self):
        # 选择第一条车辆信息
        self.click("css->#vehicleManage_tables_table > tbody > tr:nth-child(1)")

    def synch_bt_click_(self):
        # 点击同步按钮
        self.click("css->#vehicleManage_tables_div_queyFrom0_form1_button1_btn")

    def synch_YES_click(self):
        # 确认同步
        self.click("css->#layui-layer5 > div.layui-layer-btn > a.layui-layer-btn0")


