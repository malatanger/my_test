# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from common.log import Log
import time
from config import screenshot_path

success = "SUCCESS   "
fail = "FAIL      "
logger = Log()
t1 = time.time()


class Browser_engine(object):
    """浏览器引擎"""

    @staticmethod
    def my_print(msg):
        logger.info(msg)

    @staticmethod
    def get_browser(browsertype="chrome"):
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

    def open(self, url):
        """打开网址"""
        self.driver.get(url)

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
                "输入获取元素方法'id','name','class','link_text','xpath','css'.")
        return element

    def type(self, css, text):
        """输入"""
        self.get_element(css).send_keys(text)

    def close_browser(self):
        """关闭浏览器"""
        self.driver.quit()

    def F5(self):
        """刷新"""
        self.driver.refresh()

    def take_screenshot(self):
        """截图"""
        date = time.strftime('%Y%m%d%H%M%S', time.localtime())
        screenname = screenshot_path + date + ".png"
        try:
            with open(screenshot_path) as f:
                try:
                    self.driver.get_screenshot_as_file(screenname)
                    self.my_print(
                        "{0} 成功截图,地址为: {1}, 用时 {2} 秒".format(success, screenshot_path, time.time() - t1))
                except Exception:
                    self.my_print(
                        "{0} 未能截图,地址为: {1}, 用时 {2} 秒".format(fail, screenshot_path, time.time() - t1))
                    raise
        except IOError:
            self.my_print(
                "{0} 截图路径错误".format(fail)
            )

    def click(self, css):
        """点击"""
        self.get_element(css).click()


'''
if __name__ == "__main__":
    # dr = Browser_engine()
    # dr.get_browser()
    driver = pyselenium()
    driver.open("https://www.baidu.com/")
    driver.type("id->kw","123")

    driver.take_screenshot()
    driver.close_browser()
    '''
