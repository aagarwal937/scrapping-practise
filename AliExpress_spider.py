# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrappingItem

class AliexpressSpiderSpider(scrapy.Spider):
    name = 'AliExpress'
    start_urls = [
        'https://www.aliexpress.com/premium/laptop.html?d=y&origin=y&catId=0&initiative_id=SB_20200512125901&SearchText=laptop'
                  ]

    def parse(self, response):
        items = ScrappingItem()

        product_name = response.css('.item-title').css('::text').getall()
        product_rating = response.css('.rating-value').css('::text').getall()
        product_imglink = response.css('.item-img::attr(src)').getall()
        price = response.css('.price-current').css('::text').getall()


        items['product_name'] = product_name
        items['product_rating'] = product_rating
        items['price'] = price
        items['product_imglink'] = product_imglink


        yield items
