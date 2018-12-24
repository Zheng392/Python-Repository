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


class Hotel_Item_Detail(scrapy.Item):
    item_type = Field()
    detail_id = Field()
    geo_id=Field()
    name = Field()
    locality = Field()
    region = Field()
    postal_code = Field()
    country = Field()
    rating = Field()
    review_count = Field()
    price_range = Field()
    url = Field()
    rank=Field()
    traveler_photo_nums = Field()
    offical_photo_nums = Field()

class Review_Detail(scrapy.Item):
    location=Field()
    username=Field()
    title=Field()
    review_content=Field()
    hotel_id=Field()

class photo_links(scrapy.Item):
    photo_link = Field()
    hotel_id = Field()
    photo_from=Field()
