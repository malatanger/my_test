# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from common.log import Log
from selenium.webdriver.common.action_chains import ActionChains
import time
from config import screenshot_path, report_path
import os

success = "SUCCESS   "
fail = "FAIL      "
warning = "WARNING   "
logger = Log()


class Browser_engine(object):
    """浏览器引擎"""

    @staticmethod
    def my_print(msg):
        logger.info(msg)

    @staticmethod
    def get_browser(browsertype="chrome"):
        t1 = time.time()
        try:
            if browsertype == "ie":
                driver = webdriver.Ie()
            elif browsertype == "firefox":
                driver = webdriver.Firefox()
            else:
                driver = webdriver.Chrome()

            logger.info(
                "{0} 新建浏览器: {1}, 用时 {2} 秒".format(success, browsertype, time.time() - t1))
        except Exception:
            raise NameError("未发现 {0} 浏览器,你可以输入 'ie','chrome','firefox'.".format(browsertype))

        return driver


class pyselenium(Browser_engine):
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()  # 调试模式

    def open(self, url):
        """打开网址"""
        t1 = time.time()
        try:
            self.driver.get(url)
            self.my_print("{0} 成功打开链接：{1}，用时{2}.".format(success, url, time.time() - t1))
        except Exception:
            self.my_print("{0} 打开链接失败.".format(fail))
            raise

    def element_wait(self, css, sec=5):
        if not "->" in css:
            raise NameError("请在定位方法以及路径之间输入“->”")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        messages = '{0}秒内，未能找到元素：{1} '.format(sec, css)
        if by == "id":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_all_elements_located((By.ID, value)),
                messages
            )
        elif by == "name":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_element_located((By.NAME, value)),
                messages
            )
        elif by == "class":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, value)),
                messages
            )
        elif by == "link_text":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_element_located((By.LINK_TEXT, value)),
                messages
            )
        elif by == "xpath":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_element_located((By.XPATH, value)),
                messages
            )
        elif by == "css":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, value)),
                messages
            )
        else:
            raise NameError(
                "输入获取元素方法'id','name','class','link_text','xpath','css'."
            )

    def get_element(self, css):
        """获取元素"""
        global element
        if "->" not in css:
            raise NameError("请在定位方法以及路径之间输入“->”")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        # if css == "id":
        #     WebDriverWait(self.driver,5).until(lambda x:x.find_element_by_id(value))
        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "输入获取元素方法'id','name','class','link_text','xpath','css'."
            )
        return element

    def type_and_enter(self, css, text, sec):
        """输入并敲击回车"""
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.send_keys(text)
            time.sleep(sec)
            el.send_keys(Keys.ENTER)
            self.my_print(
                "{0} 元素：{1}，内容：‘{2}’输入成功，用时{3}.".format(success, css, text, time.time() - t1)
            )
        except Exception:
            self.my_print(
                "{0} 元素：{1}，内容：‘{2}’输入是吧，用时{3}.".format(fail, css, text, time.time() - t1)
            )
            raise

    def type(self, css, text):
        """输入"""
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.send_keys(text)
            self.my_print(
                "{0} 元素：{1}，内容：‘{2}’输入成功，用时{3}.".format(success, css, text, time.time() - t1)
            )
        except Exception:
            self.my_print(
                "{0} 元素：{1}，内容：‘{2}’输入是吧，用时{3}.".format(fail, css, text, time.time() - t1)
            )
            raise

    def quit(self):
        """关闭浏览器"""
        t1 = time.time()
        self.driver.quit()
        self.my_print(
            "{0} 退出浏览器并清除临时文件，用时{1}".format(success, time.time() - t1)
        )

    def F5(self):
        """刷新"""
        t1 = time.time()
        self.driver.refresh()
        self.my_print(
            "{0} 刷新页面，用时{1}".format(success, time.time() - t1)
        )

    def take_screenshot(self):
        """截图"""
        t1 = time.time()
        date = time.strftime('%Y-%m-%d')
        file_path = report_path + date + "/image/"
        isExists = os.path.exists(file_path)
        if not isExists:
            os.mkdir(file_path)
        date = time.strftime('%Y%m%d%H%M%S', time.localtime())
        screenname = file_path + date + ".png"
        try:
            picture_url = self.driver.get_screenshot_as_file(screenname)
            if picture_url is True:
                print('screenshot:  {0}.png'.format(date))
                self.my_print(
                    "{0} 截图保存成功，地址为{1},用时{2}".format(success, file_path, time.time() - t1)
                )
            else:
                self.my_print("{0} 截图保存失败.".format(warning))
        except Exception:
            raise AttributeError(
                "截图失败"
            )

    def click(self, css):
        """点击"""
        t1 = time.time()
        try:
            self.element_wait(css)
            self.get_element(css).click()
            self.my_print(
                "{0} 点击元素：{1}，用时：{2}".format(success, css, time.time() - t1)
            )
        except Exception:
            self.my_print(
                "{0} 未能点击元素{1}.".format(fail, css)
            )

    def move_to_element(self, css):
        """
        Mouse over the element.
        悬停元素。
        Usage:
        driver.move_to_element("id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).move_to_element(el).perform()
            self.my_print("{0} 移动到元素: <{1}>, 用时 {2}".format(success, css, time.time() - t1))
        except Exception:
            self.my_print("{0} 无法移动到元素: <{1}>, 用时 {2}".format(fail, css, time.time() - t1))
            raise


# if __name__ == "__main__":
#     # dr = Browser_engine()
#     # dr.get_browser()
#     driver = pyselenium()
#     driver.open("https://www.baidu.com/")
#     driver.type("id->kw","123")
#
#     driver.take_screenshot()
#     driver.close_browser()
