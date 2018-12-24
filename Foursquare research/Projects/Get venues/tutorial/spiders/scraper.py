import scrapy
import json
import re
from scrapy import Selector
from tutorial.items import *
from urllib.parse import urlencode
import yaml
import json


def get_delta(lower, upper, length):
    return (upper - lower) / length

class scraper(scrapy.Spider):
    name = "scraper"
    # base_url = "http://www.tripadvisor.cn"
    # start_urls = [
    #     base_url + "/Hotels-g297463-Chengdu_Sichuan-Hotels.html"
    # ]
    def __init__(self):

        self.venue_ids = set()
        self.allVenues = []
        self.search_count=0
        with open("config.yaml", "r") as f:
            self.cfg = yaml.load(f)
        #-
        self.lat_delta = get_delta(self.cfg['top_bound'], self.cfg['bottom_bound'], self.cfg['grid_size'])
        #+
        self.long_delta = get_delta(self.cfg['left_bound'], self.cfg['right_bound'], self.cfg['grid_size'])
    def start_requests(self):




        search_params = {
            'client_id': self.cfg['client_id'],
            'client_secret': self.cfg['client_secret'],
            'intent': 'browse',
            'limit': 50,
            'v': '20180218'
        }




        for lat in range(self.cfg['grid_size']):
            for long in range(self.cfg['grid_size']):
                ne_lat = self.cfg['top_bound'] + lat * self.lat_delta
                ne_long = self.cfg['left_bound'] + (long + 1) * self.long_delta

                search_params.update({'ne': '{},{}'.format(ne_lat, ne_long),
                                      'sw': '{},{}'.format(ne_lat + self.lat_delta,
                                                           ne_long - self.long_delta)})


                url='https://api.foursquare.com/v2/venues/search'+'?'+urlencode(search_params)

                yield scrapy.Request(url=url, callback=self.parse,meta={'ne':[ne_lat,ne_long],'cut':0})



    def parse(self, response):

        search_params = {
            'client_id': self.cfg['client_id'],
            'client_secret': self.cfg['client_secret'],
            'intent': 'browse',
            'limit': 50,
            'v': '20180218'
        }

        # hotel_urls = response.xpath('//h2[@class="listing_title"]//a[contains(@class, "property_title")]/@href').extract()
        #
        # if hotel_urls:
        #     for hotel_url in hotel_urls:
        #         hotel_completed_url = self.base_url + hotel_url
        #         yield scrapy.Request(url=hotel_completed_url,
        #                       callback=self.parse_fetch_hotel)
        #         break

        if 'venues' in json.loads(response.body)['response']:
            venues = json.loads(response.body)['response']['venues']
            if len(venues)<50:

                for venue in venues:
                    venuesItemInsta=venuesItem()
                    venuesItemInsta['venue']=venue
                    yield venuesItemInsta
            else:
                cut=response.meta['cut']
                lat_delta=(0.5**(cut+1))*self.lat_delta
                long_delta=(0.5**(cut+1))*self.long_delta
                for i in range(2):
                    for j in range(2):
                        ne_lat = response.meta['ne'][0] + i * lat_delta
                        ne_long = response.meta['ne'][1] - j * long_delta

                        search_params.update({'ne': '{},{}'.format(ne_lat, ne_long),
                                              'sw': '{},{}'.format(ne_lat + lat_delta,
                                                                   ne_long - long_delta)})

                        url = 'https://api.foursquare.com/v2/venues/search' + '?' + urlencode(search_params)

                        yield scrapy.Request(url=url, callback=self.parse, meta={'ne': [ne_lat, ne_long], 'cut': cut+1})


            self.search_count += 1
            print("search count: {};  Venues number: {} cut: {}".format(self.search_count, len(venues),response.meta['cut']))




