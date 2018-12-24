# -*- coding:utf-8 -*-
__author__ = 'LiuYang'
from services.xiechengservices.DriveServices import XiechengDriverService

class DriverServiceTest(object):

    def __init__(self):
            self.xiechengDriverService = XiechengDriverService()

    def crawlxiechengTest(self):
            self.xiechengDriverService.start()
            self.xiechengDriverService.depose()


if __name__ == "__main__":

    driverServiceTest = DriverServiceTest()

    driverServiceTest.crawlxiechengTest()