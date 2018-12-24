# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from jd_spider.items import goodsItem, commentItem
from scrapy.selector import Selector
import re
import json
import xlrd
import sys
import re
from urllib.parse import urlencode
class comment_spider(Spider):
    name = "comment2"
    IDs = []
    file = open("./data/women_cloth_data.json", 'r')
    for line in file:
        line = line.strip()
        try:  # try parsing to dict
            a = json.loads(line)
            IDs.append(a["ID"])
        except:
            print(repr(line))
            print(sys.exc_info())
            print("fail")
    file.close()
    url = 'https://club.jd.com/comment/skuProductPageComments.action'
    data = {
        'callback': 'fetchJSON_comment98vv61',
        'productId': '3555984',
        'score': 0,  # all 0 bad 1 mid 2 good 3 zhuiping 5
        'sortType': 5,  # time series rank 6 recommend rank 5
        'pageSize': 10,
        'isShadowSku': 0,
        'page': 0
    }
    start_urls = []
    for ID in IDs:
        try:
            data["productId"] = ID[0]
        except:
            pass
        for page in range(1,6):
            data['page']=page
            data['score'] = 1
            comb_url=url+'?'+urlencode(data)
            start_urls.append(comb_url)
            data['score'] = 3
            comb_url = url + '?' + urlencode(data)
            start_urls.append(comb_url)

    # name = "comment2"
    # xlrd.Book.encoding = "utf-8"
    # data = xlrd.open_workbook("goods.xls")
    # # goods为要抓取评论的商品信息，现提供一个goods.xls文件供参考,第1列：商品ID；第2列：商品评论数；第3列：商品的commentVersion
    # # test.xlsx也可以使用
    # table = data.sheets()[0]
    # nrows = table.nrows  # 行数
    # ncols = table.ncols  # 列数
    # good_id = table.col_values(0)  # 商品ID
    # comment_n = table.col_values(1)  # 商品评论数
    # comment_V = table.col_values(2)  # 商品评论的commentVersion
    #
    # start_urls = []
    # for i in range(len(good_id)):  # 一件商品一件商品的抽取
    #     good_num = int(good_id[i])
    #     comment_total = int(comment_n[i])
    #     if comment_total % 10 == 0:  # 算出评论的页数，一页10条评论
    #         page = comment_total/10
    #     else:
    #         page = comment_total/10 + 1
    #     for k in range(0, int(page)):
    #         url = "http://sclub.jd.com/productpage/p-" + str(good_num) + "-s-0-t-3-p-" + str(k) \
    #               + ".html?callback=fetchJSON_comment98vv" #+ str(comment_V[i])
    #         start_urls.append(url)

    def parse(self, response):
        m = re.search(r'(?<=fetchJSON_comment98vv61\().*(?=\);)', response.body.decode('gbk',errors='ignore')).group(0)
        j = json.loads(m)
        commentSummary = j['comments']
        items = []
        for comment in commentSummary:
            item1 = commentItem()
            item1['user_name'] = comment['nickname']
            item1['user_ID'] = comment['id']
            item1['userProvince'] = comment['userProvince']
            item1['content'] = comment['content'].replace('\n','')
            item1['good_ID'] = comment['referenceId']
            item1['userClientShow'] = comment['userClientShow']
            item1['good_name'] = comment['referenceName']
            item1['date'] = comment['referenceTime']
            item1['replyCount'] = comment['replyCount']
            item1['score'] = comment['score']
            item1['uselessVoteCount']=comment["uselessVoteCount"]
            item1['usefulVoteCount']=comment['usefulVoteCount']
            # item1['status'] = comment['status']
            # title = ""
            # if 'title'in comment:
            #     item1['title'] = comment['title']
            # item1['title'] = title
            # item1['userRegisterTime'] = comment['userRegisterTime']
            # item1['productColor'] = comment['productColor']
            # item1['productSize'] = comment['productSize']
            # item1['userLevelName'] = comment['userLevelName']
            # item1['isMobile'] = comment['isMobile']
            # item1['days'] = comment['days']
            # tags = ""
            # if 'commentTags' in comment:
            #     for i in comment['commentTags']:
            #         tags = tags + i['name'] + " "
            # item1['commentTags'] = tags
            #items.append(item1)
            yield item1
