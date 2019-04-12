# coding:utf-8
from common.basepage import pyselenium


class Hunan_pages_login(pyselenium):
    """登录"""

    def open_Hunan(self, URL):
        self.open(URL)

    def username_input(self, username):
        self.input("css->#txtUser", username)

    def password_input(self, password):
        self.input("css->#txtPwd", password)

    def click_login(self):
        self.click("css->.login-btn")


class Hunan_pages_BaseInfo(pyselenium):
    """
    基本信息车辆管理
    carinfo* -- 车辆基本信息

    """

    def move_settings(self):
        self.move_to_element("css->#home-down-icon-level")

    def baseinfo_click(self):
        """点击基本信息"""
        self.click("css->#base_info_level")

    def carinfo_carnum_input(self, car_numeber):
        """输入车牌号"""
        self.input("css->#vehicleManage_tables_div_queyFrom0_form0_text0_show", car_numeber)

    def carinfo_select_bt_click(self):
        """查询"""
        self.click("css->#vehicleManage_tables_div_queyFrom0_form1_button0_btn")

    def carinfo_chooseinfo_click(self):
        """选择第一条车辆信息"""
        self.click("css->#vehicleManage_tables_table > tbody > tr:nth-child(1)")

    def carinfo_synch_bt_click_(self):
        """点击同步按钮"""
        self.click("css->#vehicleManage_tables_div_queyFrom0_form1_button1_btn")

    def carinfo_synch_YES_click(self):
        """"确认同步"""
        self.click("css->#layui-layer5 > div.layui-layer-btn > a.layui-layer-btn0")

    def carinfo_area_input(self, area):
        """输入地区"""
        self.clear_input("css->input#vehicleManage_tables_div_queyFrom0_form0_text1_show", area)
        # self.wait(5)
        self.click("xpath->//li[contains(text(),'{0}')]".format(area))
        # self.click("xpath->//*[@class='ui-menu-item']")

    def carinfo_platform_input(self, plantform):
        """输入接入平台"""
        self.input("css->#vehicleManage_tables_div_queyFrom0_form0_text3_show", plantform)
        self.click("xpath->//li[contains(text(),'{0}')]".format(plantform))

    def carinfo_company_input(self, company):
        """输入企业"""
        self.input("css->#vehicleManage_tables_div_queyFrom0_form0_text2_show", company)
        self.click("xpath->//li[contains(text(),'{0}')]".format(company))

    def carinfo_cartype_click(self):
        """点击车辆类型选择框"""
        self.click("css->#vehicleManage_tables_div_queyFrom0_form0_select0 > input")

    def carinfo_cartype_choose(self, cartype):
        """选择车辆类型"""
        self.click("xpath->//li[contains(text(),'{0}')]".format(cartype))

    def carinfo_deletcheck_click(self):
        """删除条件选择"""
        self.click("css->#vehicleManage_tables_div_queyFrom0_form0_checkBox0_check")

    def carinfo_carstate_click(self):
        """点击状态选择框"""
        self.click("css->#vehicleManage_tables_div_queyFrom0_form0_select2 > input")

    def carinfo_carstate_choose(self, carstate):
        # self.get_text("xpath->//div/ul/li[contains(text(),'{0}')]".format(carstate))
        self.click(
            "xpath->//*[@id='vehicleManage_tables_div_queyFrom0_form0_select2']/ul/li[contains(text(),'{0}')]".format(
                carstate))


class Hunan_pages_Statistic(pyselenium):
    """
    统计分析
    installareadata* - 地区汇总
    """

    def statistic_bt_click(self):
        # self.click("css->ul.left-ico-list > li[data-control='home_tjfx'] > a.page-load[modular-name='统计分析']")
        self.click("xpath->//*[@id='home-main']/div[1]/ul[2]/li[4]/a")

    def installareadata_select_bt_click(self):
        """点击查询"""
        self.click("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_button1_btn")

    def installareadata_area_input(self, area):
        """输入地区"""
        self.clear_input("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_text0_show", area)
        self.click(
            "xpath->//*[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                area))

    def installareadata_btime_input(self, btime):
        """开始时间和结束时间"""
        # self.clear("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_datePeriod0_date0_txt")
        self.clear_input_enter("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_datePeriod0_date0_txt",
                               btime)

    def installareadata_etime_input(self, etime):
        self.clear_input_enter("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_datePeriod0_date1_txt",
                               etime)

    def installareadata_cartype_click(self):
        self.click("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_vehicleTypeTree0 > input")

    def installareadata_cartype_check(self, cartype):
        self.click("xpath->//li[contains(text(),'{0}')]".format(cartype))


class Hunan_pages_Assessment(pyselenium):
    """
    考核通报
    areaassessment_mouth* - 地区考核月度查询
    areaassessment_year* - 地区考核年度查询
    areaassessment_day* - 地区考核实时查询
    """

    def assessment_bt_click(self):
        self.click("xpath->//*[@id='home-main']/div[1]/ul[2]/li[1]/a")

    def areaassessment_select_bt_click(self):
        self.click("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_button1_btn")

    def areaassessment_type_choose(self, areaassessmenttype):
        """选择考核类型"""
        self.click("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_select0 > input")
        self.click("xpath->//li[contains(text(),'{0}')]".format(areaassessmenttype))

    def areaassessment_area_input(self, area):
        """输入地区"""
        self.clear_input("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_text0_show", area)
        # report_zoneCheckRank_table_div_tabs0_content_panel0_form0_text0_show
        self.click(
            "xpath->//*[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                area))

    def areaassessment_mouth_time_input(self, time):
        """输入时间（月）"""
        self.clear_input_enter("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_date0_txt", time)

    def areaassessment_year_time_input(self, time):
        """输入时间（年）"""
        self.clear_input_enter("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_date1_txt", time)

    def areaassessment_cartype_click(self):
        """点击车辆类型"""
        self.click("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_select1 > input")

    def areaassessment_cartype_check(self, cartype):
        """选择车辆类型"""
        self.click("xpath->//li[contains(text(),'{0}')]".format(cartype))

    def areaassessment_btime_input(self, btime):
        self.clear_input_enter("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_datePeriod0_date0_txt",
                               btime)

    def areaassessment_etime_input(self, etime):
        self.clear_input_enter("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_datePeriod0_date1_txt",
                               etime)
