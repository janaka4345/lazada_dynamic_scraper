import scrapy


class LazadaspiderSpider(scrapy.Spider):
    name = "lazadaspider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
