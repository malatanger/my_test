# coding:utf-8
from common import HTMLTestRunner_Spare,HTMLTestRunner
import unittest
from config import testcase_paht, report_path
import os
import time


def run():
    discover = unittest.defaultTestLoader.discover(
        testcase_paht,
        "test_Hunan*"
    )
    date = time.strftime('%Y-%m-%d')
    file_path = report_path  + date + "/"
    isExists = os.path.exists(file_path)
    if not isExists:
        os.mkdir(file_path)
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = file_path + 'TestResult-' + now + '.html'
    with open(reportname, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='执行人： JS',
            tester = '井松'
        )
        runner.run(discover)

if __name__ == "__main__":
    run()
