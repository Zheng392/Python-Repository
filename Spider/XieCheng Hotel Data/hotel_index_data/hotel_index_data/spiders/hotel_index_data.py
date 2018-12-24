
from scrapy.spiders import Spider
from scrapy import *
from scrapy.selector import Selector
import re
import json
import xlrd
import sys
import re
from urllib.parse import urlencode
class hotel_index_data(Spider):
    name='hotel_index_data'
    def start_requests(self):
        url = "https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx"
        data = {'page': '1', 'cityPY': 'shanghai', 'cityId': '2', 'cityCode': '021',

                }
        headers = {'Referer': 'http://hotels.ctrip.com/hotel/shanghai2',
                              'Accept': '* / *', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Host': 'hotels.ctrip.com', 'Origin': 'http://hotels.ctrip.com',
                   'Proxy-Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
                   }
        yield Request(url, self.parse, method="POST", headers=headers, body=json.dumps(data))

    def parse(self, response):
        data = json.loads(response.body)
        print(data)