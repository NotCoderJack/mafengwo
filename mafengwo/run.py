# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from mafengwo.spiders.mafengwo_spider import MafengwoSpider

settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl(MafengwoSpider)

process.start()
