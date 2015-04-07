import scrapy

class NarSpider(scrapy.Spider):
    name = "nar"
    allowed_domains= "http://newalbumreleases.net/"
    start_urls = [
            "http://newalbumreleases.net/category/indie/",
    ]

    def parse(self, response):
        for sel in response.xpath('//h2/a'):
            title = sel.xpath('text()').extract()
            print title
