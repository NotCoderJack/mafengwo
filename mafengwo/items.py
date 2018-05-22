# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StateItem(scrapy.Item):
    """
    Description : 马蜂窝全球目的地数据
    """
    # 页面地址
    url = scrapy.Field()
    # 目的地ID
    state_id = scrapy.Field()
    chinese_name = scrapy.Field()
    english_name = scrapy.Field()
    # 目的地图片页面地址
    photo_url = scrapy.Field()
    # 百科地址
    baike_url = scrapy.Field()
    # 游记地址
    youji_url = scrapy.Field()
    pass


class CityListItem(scrapy.Item):
    """
    Description : 热门城市列表
    """
    # 所在国家ID
    state_id = scrapy.Field()
    # 热门城市ID列表
    city_num = scrapy.Field()
    city_ids = scrapy.Field()
    pass

class CitySumItem(scrapy.Item):
    """
    Description : state的热门城市列表页城市数据汇总
    """
    state_id = scrapy.Field()
    city_id = scrapy.Field()
    url = scrapy.Field()
    chinese_name = scrapy.Field()
    english_name = scrapy.Field()
    # main photo
    city_photo_url = scrapy.Field()
    city_sum = scrapy.Field()
    # 热度，多少人去过
    hot_index = scrapy.Field()
    # top3 景点名称及ID
    top3_attraction = scrapy.Field()
    pass

class Top3AttractionItem(scrapy.Item):
    attraction_name = scrapy.Field()
    attraction_id = scrapy.Field()
    attraction_url = scrapy.Field()

class CityItem(scrapy.Item):
    city_id = scrapy.Field()
    photo_url = scrapy.Field()
    # 概况页面地址
    baike_url = scrapy.Field()
    # 景点地址
    attraction_url = scrapy.Field()
    # 游记地址
    youji_url = scrapy.Field()
    #
    # 周边城市列表
    nearby_cities = scrapy.Field()
    pass


class NearbyCityItem(scrapy.Item):
    city_id = scrapy.Field()
    url = scrapy.Field()
    photo_url = scrapy.Field()
    name = scrapy.Field()
    hot_index = scrapy.Field()
    pass


