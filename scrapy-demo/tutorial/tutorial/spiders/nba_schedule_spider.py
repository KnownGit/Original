#!/usr/bin/env python
#-*- coding: utf-8 -*-
import scrapy

class NBAScheduleSpider(scrapy.Spider):
    name = "nba-schedule"
    start_urls = [
        "https://nba.hupu.com/schedule",
    ]

    def parse(self, response):

        players_table = response.xpath('//table[@class="players_table"]/tbody/tr[contains(@class, "left")]')

        current_time = ""
        for item in players_table:

            if len(item.xpath('./td[@colspan="3"]')) > 0:
                print u'比赛日期: ' + item.xpath('./td[@colspan="3"]/text()').extract_first()                
            else:
                time = item.xpath('./td[@class="left"]/text()').extract_first()
                guest = item.xpath('./td/a[1]/text()').extract_first()
                home = item.xpath('./td/a[2]/text()').extract_first()

                print time + " " + guest + "vs" + home

            print '\n'