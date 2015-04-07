# -*- coding: utf-8 -*-

import scrapy


class NarItem(scrapy.Item):
    artist = scrapy.Field()
    album = scrapy.Field()
    download_url = scrapy.Field()
