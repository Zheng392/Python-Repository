# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
import json

from twisted.enterprise import adbapi

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy import log
# import chardet

SETTINGS = get_project_settings()


class MySQLPipeline(object):

    def __init__(self):
        # Instantiate DB
        self.file=open('men_cloth_data.json', 'w', encoding='utf-8')
        # self.dbpool = adbapi.ConnectionPool('pymysql',
        #                                     host=SETTINGS['DB_HOST'],
        #                                     user=SETTINGS['DB_USER'],
        #                                     passwd=SETTINGS['DB_PASSWD'],
        #                                     port=SETTINGS['DB_PORT'],
        #                                     db=SETTINGS['DB_DB'],
        #                                     charset='utf8',
        #                                     use_unicode=True,
        #                                     cursorclass=pymysql.cursors.DictCursor
        #                                     )
        # self.stats = stats
        # dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        print("done!!!")

        """ Cleanup function, called after crawing has finished to close open
            objects.
            Close ConnectionPool. """
        # self.dbpool.close()

    def process_item(self, item, spider):
        line=json.dumps(dict(item,ensure_ascii=False))+'\n'
        self.file.write(line)

        # query = self.dbpool.runInteraction(self._insert_record, item)
        # query.addErrback(self._handle_error)
        return item


    def _handle_error(self, e):
        log.err(e)

