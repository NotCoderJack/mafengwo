"""
Description : Crawl mafengwo site pages
"""
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from mafengwo.items import StateItem
from mafengwo.items import CityListItem
from mafengwo.items import CitySumItem
from mafengwo.items import Top3AttractionItem
from mafengwo.items import CityItem
from mafengwo.items import NearbyCityItem
import re


class MafengwoSpider(CrawlSpider):

    name = "mafengwo"
    TARGET_SITE_HOST = "http://www.mafengwo.cn"
    allowed_domains = ['mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/mdd']
    rules = (
        Rule(LinkExtractor(allow=('/travel-scenic-spot/mafengwo/10180.html'), restrict_css='div.row-state'),
             process_links="process_links", callback="parse_state", follow=True),
        Rule(LinkExtractor(allow=('/mdd/citylist/\d{5}.html'), restrict_css='div.place-navbar'),
             process_links="process_links", callback="parse_citylist", follow=True),
        Rule(LinkExtractor(allow=('/travel-scenic-spot/mafengwo/\d{5}.html'), restrict_css='ul#citylistlist li.item'),
             process_links="process_links", callback="parse_city")
    )

    def process_links(self, links):
        for i, w in enumerate(links):
            w.url = re.sub("[\t|\r|\n|\s+]", "", w.url)
            links[i] = w
        return links

    def parse_state(self, response):
        item = StateItem()
        url = response.url
        item['url'] = url
        item['state_id'] = self.get_page_name(url)
        item['chinese_name'] = response.css('div.title h1::text').extract_first()
        item['english_name'] = response.css('span.en::text').extract_first()
        item['photo_url'] = response.css('a.num-photo::attr(href)').extract_first()
        item['baike_url'] = response.css('a.navbar-btn::attr(href)').extract_first()
        item['youji_url'] = response.css('li.navbar-community div.navbar-dropmenu.hide ul.navbar-sub a::attr(href)').extract_first()
        print(item)
        yield item

    def parse_citylist(self, response):
        cityListItem = CityListItem()
        state_id = self.get_page_name(response.url)
        cityListItem['state_id'] = state_id
        cityListItem['city_num'] = response.css('div.row-placeList div.hd h3 em::text').extract_first()
        cityListItem['city_ids'] = response.css('div.row-placeList div.bd ul#citylistlist li.item div.img a::attr(data-id)').extract()
        # process pagination data here
        print(cityListItem)
        # 获取当页数据(第一页数据)
        items = response.css('div.row-placeList div.bd ul#citylistlist li.item')
        for item in items:
            citySumItem = self.parse_citysum(item, state_id)
            print(citySumItem)

        print(cityListItem)
        # yield cityListItem

    def parse_citysum(self, item, state_id):
        citySumItem = CitySumItem()
        citySumItem['state_id'] = state_id
        citySumItem['city_id'] = item.css('div.img a::attr(data-id)').extract_first()
        citySumItem['url'] = item.css('div.img a::attr(href)').extract_first()
        citySumItem['chinese_name'] = item.css('div.img div.title::text').extract_first().strip()
        citySumItem['english_name'] = item.css('div.img div.title p.enname::text').extract_first()
        citySumItem['city_photo_url'] = item.css('div.img img::attr(data-original)').extract_first()
        citySumItem['city_sum'] = item.css('div.detail::text').extract_first().strip()
        citySumItem['hot_index'] = item.css('dl.caption div.nums b::text').extract_first()

        top3 = item.css('dl.caption dd a')
        top3list = []
        for t in top3:
            top3Item = Top3AttractionItem()
            top3Item['attraction_name'] = t.css('::attr(title)').extract_first()
            top3Item['attraction_id'] = t.css('::attr(data-id)').extract_first()
            top3Item['attraction_url'] = t.css('::attr(href)').extract_first()
            top3list.append(top3Item)

        citySumItem['top3_attraction'] = top3list
        return citySumItem

    def request_city(self, url):
        print(self.TARGET_SITE_HOST + url)
        request = scrapy.Request(url = self.TARGET_SITE_HOST + url, callback=self.parse_city)
        yield request
        # yield

    def parse_city(self, response):
        cityItem = CityItem()
        cityItem['city_id'] = self.get_page_name(response.url)
        cityItem['photo_url'] = response.css('a.num-photo::attr(href)').extract_first()
        cityItem['baike_url'] = response.css('li.city-guide a.navbar-btn::attr(href)').extract_first()
        cityItem['youji_url'] = response.css('li.navbar-community a[href*="yj"]::attr(href)').extract_first()
        cityItem['attraction_url'] = response.css('li.navbar a.navbar-btn::attr(href)').extract_first()

        cityItem['nearby_cities'] = []
        # async method get nearby cities

    def parse_attraction(self, response):
        return

    def get_page_name(self, url):
        return re.search(r'(\d+).html$', url).group(1)