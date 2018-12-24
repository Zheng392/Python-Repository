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
        self.hotel_detail = open('hotel_detail.json', 'w', encoding='utf-8')
        self.review_file=open('review.json','w',encoding='utf-8')
        self.photo_file = open('photo.json', 'w', encoding='utf-8')

   	def close_spider(self, spider):
   		self.hotel_detail.close()
        self.review_file.close()
        self.photo_file.close()


    def process_item(self, item, spider):
        if isinstance(item,Hotel_Item_Detail):
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.hotel_detail.write(line)

        elif isinstance(item,photo_links):
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.photo_file.write(line)

        else:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.review_file.write(line)


        return item
