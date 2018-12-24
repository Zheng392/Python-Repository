import scrapy
import json
import re
from scrapy import Selector
from tutorial.items import *
from urllib.parse import urlencode

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept - Encoding':'gzip, deflate, br',
               'Accept-Language':'en-US,en;q=0.9',
               'Connection':'Keep-Alive',
	      'Cache-Control': 'max-age=0',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

class scraper(scrapy.Spider):
    name = "scraper"
    base_url = "http://www.tripadvisor.cn"

    def __init__(self):

        self.hotel_photo_links=[]
        
    def start_requests(self):
	    yield scrapy.Request(url=self.base_url+"/Hotels-g297463-Chengdu_Sichuan-Hotels.html", callback=self.parse)

    

    def parse(self, response):



        hotel_urls = response.xpath('//h2[@class="listing_title"]//a[contains(@class, "property_title")]/@href').extract()

        if hotel_urls:
            for hotel_url in hotel_urls:
                hotel_completed_url = self.base_url + hotel_url
                yield scrapy.Request(url=hotel_completed_url,
                              callback=self.parse_fetch_hotel)
                break



    def parse_fetch_hotel(self, response):
        hxs=Selector(response)

        hi = Hotel_Item_Detail()

        hi['item_type'] = 'hotel'
        hi['detail_id'] = re.search('d[0-9]+', response.url).group(0).strip('d')
        hi['geo_id']=re.search('g[0-9]+',response.url).group(0).strip('g')
        hi['name'] = hxs.xpath( '//h1[contains(@id, "HEADING")]/text()').extract()[0]
        hi['url'] = response.url
        hi['rank']=hxs.xpath('//*[@id="taplc_location_detail_header_hotels_0"]//div/span/b/text()').extract()[0]
        hi['traveler_photo_nums']=int(re.search('[0-9]+',
                                       hxs.xpath('//*[@id="taplc_hr_atf_north_star_nostalgic_0"]//div[@class="albumInfo"]/text()').extract()[0]).group(0))
        hi['offical_photo_nums']=int(re.search('[0-9]+',
                                       hxs.xpath('//*[@id="taplc_hr_atf_north_star_nostalgic_0"]//span[@class="see_all_count"]/text()').extract()[0]).group(0))\
                                 -hi['traveler_photo_nums']
        yield hi

        for count,j in enumerate(['offical_photo_nums','traveler_photo_nums']):
            for i in range(int(hi[j]/50)+1):
                headers={
                    'geo':hi['geo_id'],
                    'detail':hi['detail_id'],
                    'albumViewMode':'images',
                    'aggregationId':101,
                    'albumid':101,
                    'cnt':50,
                    'offset': 50*i,
                    'filter':count+1,
                    'albumPartialsToUpdate':'partial',
                }
                photo_url='https://www.tripadvisor.cn/LocationPhotoAlbum?'+urlencode(headers)
                yield scrapy.Request(photo_url,self.parse_fetch_photo,
                                     meta={'id':hi['detail_id'],'count':count})
                break




        #get review
        pages=hxs.xpath('//*[@id="taplc_location_reviews_list_hotels_0"]//div[@class="pageNumbers"]/span[@class="pageNum last taLnk "]/@data-page-number').extract()[0]
        pages=int(pages)
        for i in range(pages):
            split = response.url.split('Reviews')
            review_page_url = ('Reviews-or' + str(i * 5)).join(split)
            yield scrapy.Request(review_page_url,self.parse_review,meta={'id':hi['detail_id']})
            if i > 2:
                break



    def parse_fetch_photo(self,response):
        photos=photo_links()

        sel=Selector(response)
        photo_link=sel.xpath('//img[@onload]/@src').extract()
        if response.meta['count']==0:
            photos['photo_from']='official'
        else:
            photos['photo_from'] = 'traveler'
        photos['hotel_id'] =response.meta['id']

        temp=[]
        for i in photo_link:
            temp.append(i)
        photos['photo_link']=temp



        yield photos


    def parse_review(self,response):
        pass

        sel=Selector(response)


        username=sel.xpath('//*[@id="taplc_location_reviews_list_hotels_0"]//div[@class="review-conta'
                           'iner"]//span[@class="expand_inline scrname"]/text()').extract()
        location=sel.xpath('//*[@id="taplc_location_reviews_list_hotels_0"]//div[@class="review-conta'
                           'iner"]//span[@class="expand_inline userLocation"]/text()').extract()
        title=sel.xpath('//*[@id="taplc_location_reviews_list_hotels_0"]//div[@class="review-container"]'
                        '//span[@class="noQuotes"]/text()').extract()
        review_content=sel.xpath('//*[@id="taplc_location_reviews_list_hotels_0"]//div[@class="review-container"]'
                         '//div[@class="wrap"]/div[@class="prw_rup prw_reviews_text_summary_hsx"]'
                         '/div/p[@class="partial_entry"]/text()').extract()

        for i in range(len(review_content)):
            Reviews = Review_Detail()
            Reviews['location']=location[i]
            Reviews['username'] = username[i]
            Reviews['title'] = title[i]
            Reviews['review_content'] = review_content[i]
            Reviews['hotel_id']=response.meta['id']
            yield Reviews




