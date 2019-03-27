# coding:utf-8
from common.basepage import pyselenium

class Ganzhou_pages_login(pyselenium):

    def open_Ganzhou(self):
        self.open("http://111.75.255.103/")

    def type_username(self):
        self.type("css->#txtUser","js001")
    def type_password(self):
        self.type("css->sdfa")