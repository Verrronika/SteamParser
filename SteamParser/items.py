import scrapy

class SteamparserItem(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    number_of_reviews = scrapy.Field()
    raiting = scrapy.Field()
    data = scrapy.Field()
    developer = scrapy.Field()
    tags = scrapy.Field()
    price = scrapy.Field()
    platforms = scrapy.Field()
