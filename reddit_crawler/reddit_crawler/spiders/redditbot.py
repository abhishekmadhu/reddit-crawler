# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones/']

    def parse(self, response):
        titles = response.css(".ILDoH::text").extract()
        votes = response.css("._1rZYMD_4xY3gRcSS3p8ODO::text").extract()
        # there are dual entries of each vote count on each page (why the F?)
        # cleanup begins
        for i in range(0, int(len(votes)/2)):
            votes[i] = votes[2*i]

        # times = response.css('time::attr(title)').extract()
        # comments = response.css('.comments::text').extract()

        for item in zip(titles, votes):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title': item[0],
                'vote': item[1]
                # 'created_at': item[2],
                # 'comments': item[3],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
