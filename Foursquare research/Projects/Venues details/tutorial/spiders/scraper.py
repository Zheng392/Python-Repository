import scrapy
import json
import re
from scrapy import Selector
from tutorial.items import *
from urllib.parse import urlencode
import yaml
import json
import pandas as pd
import numpy as np
import re

def get_delta(lower, upper, length):
    return (upper - lower) / length

class scraper(scrapy.Spider):
    name = "scraper"
    # base_url = "http://www.tripadvisor.cn"
    # start_urls = [
    #     base_url + "/Hotels-g297463-Chengdu_Sichuan-Hotels.html"
    # ]
    with open("config.yaml", "r") as f:
        cfg = yaml.load(f)
    search_params = {
        'client_id': cfg['client_id'],
        'client_secret': cfg['client_secret'],
        'v': '20180218'
    }
    start_urls = []

    df=pd.read_csv('data.csv',encoding='utf-8')
    df=df.sort_values(by='checkinsCount',ascending=False)
    ids=list(df['id'][0:500].values)
    for id in ids:
        url = 'https://api.foursquare.com/v2/venues/{}'.format(id) + '?' + urlencode(search_params)
        start_urls.append(url)


    def __init__(self):

        self.venue_ids = set()
        self.allVenues = []
        self.search_count=0
        with open("config.yaml", "r") as f:
            cfg = yaml.load(f)
        self.photosParams = {
            'client_id': cfg['client_id'],
            'client_secret': cfg['client_secret'],
            'v': '20180218',
            "limit": 200

        }
        self.tipsParams = {
            'client_id': cfg['client_id'],
            'client_secret': cfg['client_secret'],
            'v': '20180218',
            "limit":200
        }


    def parse(self, response):

        if 'venue' in json.loads(response.body)['response']:
            venue = json.loads(response.body)['response']['venue']
            photosNum=venue['photos']['count']
            tipsNum=venue['stats']['tipCount']
            venuesItemInsta=venuesItem()
            venuesItemInsta['venue']=venue
            yield venuesItemInsta

            self.search_count += 1
            print("search count: {}; ".format(self.search_count))

            for photosCount in range(int(photosNum/200)+1):
                self.photosParams.update({"offset":200*photosCount})
                yield scrapy.Request(url=response.url.split('?')[0]+'/photos?'+ urlencode(self.photosParams),
                                     callback=self.ParsePhotos)


            for tipsCount in range(int(tipsNum/200)+1):
                self.tipsParams.update({"offset":200*tipsCount})
                yield scrapy.Request(url=response.url.split('?')[0]+'/tips?'+ urlencode(self.tipsParams),
                                     callback=self.ParseTips)



    def ParsePhotos(self, response):
        if 'photos' in json.loads(response.body)['response']:
            photos=json.loads(response.body)['response']['photos']['items']
            id=re.search('(venues/)(.*?)(/photo)',response.url).group(2)
            for photo in photos:
                photosItemInst=photosItem()
                photosItemInst['photo']=photo
                photosItemInst['id']=id
                yield photosItemInst

            self.search_count += 1
            print("search count: {}; ".format(self.search_count))



    def ParseTips(self, response):
        if 'tips' in json.loads(response.body)['response']:
            tips=json.loads(response.body)['response']['tips']['items']
            id=re.search('(venues/)(.*?)(/tips)',response.url).group(2)
            for tip in tips:
                tipsItemInst=tipsItem()
                tipsItemInst['tip']=tip
                tipsItemInst['id']=id
                yield tipsItemInst

            self.search_count += 1
            print("search count: {}; ".format(self.search_count))