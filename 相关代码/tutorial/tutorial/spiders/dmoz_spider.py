import scrapy
from tutorial.items import DoubanItem
from scrapy.selector import Selector
from scrapy.http import Request
from urllib.parse import urljoin

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/top250",
    ]
    def parse(self, response):
        item=DoubanItem()
        selector=Selector(response)
        Movies=selector.xpath('//div[@class="info"]')
        for each in Movies:
            title=each.xpath('div[@class="hd"]/a/span/text()').extract()[0]
            star=each.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[0]
            item['title']=title
            item['star']=star
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink=nextLink[0]
            yield Request(urljoin(response.url,nextLink),callback=self.parse)

        