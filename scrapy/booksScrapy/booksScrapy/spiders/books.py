import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            yield {
                'titulo': book.css('h3 a::attr(title)').get(),
                'preco': book.css('.price_color::text').get(),
                'imagemCapa': response.urljoin(book.css('img::attr(src)').get())
            }
        pass
