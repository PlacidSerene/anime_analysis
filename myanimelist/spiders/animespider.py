import scrapy

class AnimeSpider(scrapy.Spider):
    name = 'anime'
    start_urls = ['https://myanimelist.net/anime/genre/1/Action']


    def parse(self, response):

        for animes in response.css('div.seasonal-anime.js-seasonal-anime'):
            yield {
                'anime_name': animes.css('a.link-title::text').get(),
                'description': animes.css('span.preline::text').get().replace('\r\n\r\n',''),
                'release date': animes.css('span.remain-time::text').get().replace('\n','').strip(),
                'time': animes.css('div.eps').css('span::text').get().replace(' eps',''),
                'studio': animes.css('span.producer').css('a::text').get(),
                'views': animes.css('span.member.fl-r::text').get().replace('\n','').strip(),
                'genres': animes.css('span.genre').css('a::text').getall(),
                # 'score': animes.css('span.score.score-label.score-8::text').get().replace('\n','').strip()
            }

