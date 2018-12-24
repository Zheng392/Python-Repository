# -*- coding:utf-8 -*-
__author__ = 'LiuYang'

from services.xiechengservices.hotelInfo import XiechenghotelService

class DriverServiceTest(object):

    def __init__(self):
            self.xiechenghotelService = XiechenghotelService()

    def crawlxiechengTest(self):
            self.xiechenghotelService.getdata()
            self.xiechenghotelService.depose()



if __name__ == "__main__":

    driverServiceTest = DriverServiceTest()

    driverServiceTest.crawlxiechengTest()