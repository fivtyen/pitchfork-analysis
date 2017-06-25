# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PitchforkCrawlerItem(scrapy.Item):
    artist = scrapy.Field()
    album_name = scrapy.Field()
    genre = scrapy.Field()
    score = scrapy.Field()
    release_year = scrapy.Field()
    label = scrapy.Field()
    cover_img_url = scrapy.Field()
    review_url = scrapy.Field()
    review_author = scrapy.Field()
    review_date_day = scrapy.Field()
    review_date_month = scrapy.Field()
    review_date_year = scrapy.Field()
    merit = scrapy.Field()
    
    
