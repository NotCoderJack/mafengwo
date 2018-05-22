# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
import pymongo

settings = get_project_settings()

class MafengwoPlacePipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', settings['MONGO_URI']),
            mongo_db=crawler.settings.get('MONGO_DB', settings['MONGO_DBNAME'])
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db['place']
        post = dict(item)
        print(post)
        collection.upsert(post)
        return item
