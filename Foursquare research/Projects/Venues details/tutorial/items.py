# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass




class venuesItem(scrapy.Item):
    venue=Field()


class photosItem(scrapy.Item):
    id=Field()
    photo=Field()

class tipsItem(scrapy.Item):
    id=Field()
    tip=Field()