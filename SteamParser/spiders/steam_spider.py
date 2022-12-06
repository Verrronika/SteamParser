import scrapy
import re
from ..items import SteamparserItem

class BookSpider(scrapy.Spider):
  name = 'steam'
  allowed_domains = ['store.steampowered.com']
  
  def start_requests(self):
        search_requests = ['indie', 'гонки', 'football']
        url_pattern = 'https://store.steampowered.com/search/?term'
        
        for search_request in search_requests:
            for page_number in range(1, 10):
                yield scrapy.Request(url=f'{url_pattern}={search_request}&page={page_number}', callback=self.parse)


  def parse(self, response):
    for app_link in response.xpath('//a[contains(@href, "app")]/@href').extract():
        yield response.follow(app_link, callback=self.parse_app) 
    
        
  def parse_app(self, response):
    items = SteamparserItem()

    price = response.xpath('//div[@class="discount_final_price"]/text()').extract_first()
    if price != None:
        price = price.split('\u0443\u0431')[0]
    
    platforms = set()
    for platform in response.css('div').xpath('@data-os'):
        platforms.add(platform.get().strip())

    data = response.xpath('//div[@class="date"]/text()').extract_first()

    items['name'] = response.xpath('//span[@itemprop="name"]/text()').extract_first()
    items['category'] = response.xpath('//div[@class="blockbg"]/a/text()').extract()
    items['number_of_reviews'] = response.xpath('//meta[@itemprop="reviewCount"]/@content').extract_first()
    items['raiting'] = response.xpath('//meta[@itemprop="ratingValue"]/@content').extract_first()
    items['data'] = data
    items['developer'] = response.xpath('//div[@class="dev_row"]/a/text()').extract_first()
    items['tags'] = [el.split('\t\t\t\t\t\t\t\t\t\t\t\t')[1] for el in response.xpath('//a[@class="app_tag"]/text()').extract()]
    items['price'] = price                         
    items['platforms'] = platforms
    yield items

