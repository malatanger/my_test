# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from common.log import Log
import time
from config import screenshot_path

success = "SUCCESS   "
fail = "FAIL   "
logger = Log()


class Browser_engine(object):
    """浏览器引擎"""

    def get_browser(self, browsertype="chrome"):

        if browsertype == "ie":
            driver = webdriver.Ie()
        elif browsertype == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        return driver


class pyselenium(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

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
        self.driver.get_screenshot_as_file(screenname)

    def click(self,css):
        """点击"""
        self.get_element(css).click()

if __name__ == "__main__":
    # dr = Browser_engine()
    # dr.get_browser()
    driver = pyselenium()
    driver.open("https://www.baidu.com/")
    driver.type("id->kw","123")

    driver.take_screenshot()
    driver.close_browser()
