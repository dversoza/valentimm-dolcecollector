import scrapy


class DolcespiderSpider(scrapy.Spider):
    name = "dolcespider"
    allowed_domains = ["www.nescafe-dolcegusto.com.br"]
    start_urls = ["https://www.nescafe-dolcegusto.com.br/sabores"]

    def parse(self, response):
        pass
