import scrapy


class DolcespiderSpider(scrapy.Spider):
    name = "dolcespider"
    allowed_domains = ["www.nescafe-dolcegusto.com.br"]
    start_urls = ["https://www.nescafe-dolcegusto.com.br/sabores"]

    def parse(self, response):
        coffees = response.css(".product-card__content")
        for coffee in coffees:
            yield {
                "name": coffee.css(".product-card__name a ::text").get(),
                "price": coffee.css(".price-wrapper span ::text").get(),
                "capsules": coffee.css(".product-card__name a ::attr(href)").get(),
                "link": coffee.css("a::attr(href)").get(),
                "points": coffee.css(".product-card__price .price_pp ::text").get(),
                "description": coffee.css(".product-card__description--short ::text").get(),
            }