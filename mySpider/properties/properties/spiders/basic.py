import scrapy


ss BasicSpider(scrapy.Spider):
    name = 'basic'
    # allowed_domains = ['web']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        # parse data
        # book
        book_infos = response.xpath('//article[@class="product_pod"]')
        for book_info in book_infos:
            book_name =  book_info.xpath('//h3/a/@title')
            print(book_name,'--------------------------')

