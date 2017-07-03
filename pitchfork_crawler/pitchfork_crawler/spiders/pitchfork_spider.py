import scrapy
import datetime
from pitchfork_crawler import items


class PitchforkSpider(scrapy.Spider):
    name = 'pitchSpid'
    allowed_domains = ['pitchfork.com']
    start_urls = ['http://pitchfork.com/reviews/albums/?page=' + str(n) for n in range(1, 1586)]
    review_xpath = '//div[@class="review"]/a/@href' 
    
    
    # creating request for every album review listed on a given page
    def parse(self, response):
        for href in response.xpath(self.review_xpath):
            review_url = 'http://pitchfork.com' + href.extract()
            yield scrapy.Request(url = review_url, callback = self.parse_review)
         
         
    # parsing data from a single review        
    def parse_review(self, response):
        artist = response.xpath('//h2[@class="artists"]/ul[@class="artist-links artist-list"]/li/a/text()').extract()
        album_name = response.xpath('//h1[@class="review-title"]/text()').extract_first()
        release_year = response.xpath('//div[@class="labels-and-years"]/span[@class="year"]/text()').extract()[1]
        genre = response.xpath('//div[@class="article-meta"]/ul[@class="genre-list before"]/li/a/text()').extract()
        label = response.xpath('//div[@class="labels-and-years"]/ul[@class="label-list"]/li/text()').extract()
        score = response.xpath('//span[@class="score"]/text()').extract_first()
        merit = response.xpath('//p[@class="bnm-txt"]/text()').extract_first()
        review_author = response.xpath('//a[@class="display-name"]/text()').extract_first()
        review_date = response.xpath('//time[@class="pub-date"]/@title').extract_first()
        review_url = response.request.url
        review_author_url = 'http://www.pitchfork.com' + response.xpath('//a[@class="display-name"]/@href').extract_first()
        cover_img_url = response.xpath('//div[@class="album-art"]/img/@src').extract_first()
        
        # formatting album's name
        album_name = album_name.replace('\n', '')
        
        # date parsing
        review_date = review_date[:16].replace(',','')
        review_date = datetime.datetime.strptime(review_date, '%a %d %b %Y').strftime('%d %m %Y')
        review_date_day = review_date[0:2]
        review_date_month = review_date[3:5]
        review_date_year = review_date[6:10]
        
        # creating scrapy items
        item = items.PitchforkCrawlerItem()
        item['artist'] = artist
        item['album_name'] = album_name
        item['genre'] = genre
        item['score'] = score
        item['merit'] = merit
        item['release_year'] = release_year
        item['label'] = label
        item['cover_img_url'] = cover_img_url
        item['review_author'] = review_author
        item['review_date_day'] = review_date_day
        item['review_date_month'] = review_date_month
        item['review_date_year'] = review_date_year
        item['review_url'] = review_url
        
        yield item
        