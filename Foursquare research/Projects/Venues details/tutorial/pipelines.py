# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial.items import *
import json

class TutorialPipeline(object):
    def __init__(self):
        self.count = 0
        self.hotel_detail_all = []
        self.review_all=[]

    def open_spider(self, spider):
        self.venues = open('venues.json', 'w', encoding='utf-8')
        self.photosFile=open('photosData.json','w',encoding='utf-8')
        self.tipsFile = open('tipsData.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.venues.close()
        self.photosFile.close()
        self.tipsFile.close()

    def process_item(self, item, spider):
        if isinstance(item,venuesItem):
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.venues.write(line)

        elif isinstance(item,photosItem):
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.photosFile.write(line)

        else:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.tipsFile.write(line)


        return item
