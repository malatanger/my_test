# coding:utf-8
from common.basepage import pyselenium
from common.get_parameter import ExcelUtil
from config import datas_path

data = ExcelUtil(datas_path + "Hunan_datas.xlsx", "Sheet1")
para = data.dict_data()


class Hunan_pages_login(pyselenium):
    """登录"""

    def open_Hunan(self,URL):

        self.open(URL)

    def type_username(self,username):
        self.type("css->#txtUser", username)

    def type_password(self,password):
        password = para[0]["password"]
        self.type("css->#txtPwd", password)

    def click_login(self):
        self.click("css->.login-btn")


class Hunan_pages_Synch(pyselenium):
    """同步车辆基本信息"""

    def move_to_settings(self):
        self.move_to_element("css->#home-down-icon-level")

    def click_basicinformation(self):
        self.click("css->#base_info_level")

    def type_carNums(self):
        for i in range(5):
            carNUM = para[i]["carNUM"]
            self.type("css->#vehicleManage_tables_div_queyFrom0_form0_text0_show", carNUM)
            i += 1

    def type_carNum(self,car_numeber):
        self.type("css->#vehicleManage_tables_div_queyFrom0_form0_text0_show", car_numeber)

    def click_select_bt(self):
        self.click("css->#vehicleManage_tables_div_queyFrom0_form1_button0_btn")

    def click_carinfo(self):
        self.click("css->#vehicleManage_tables_table > tbody:nth-child(1) > tr:nth-child(1)")

    def click_synch_bt(self):
        self.click("css->#vehicleManage_tables_div_queyFrom0_form1_button1_btn")

    def click_YES(self):
        self.click("css->#layui-layer5 > div.layui-layer-btn > a.layui-layer-btn0")
