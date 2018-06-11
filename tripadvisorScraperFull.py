#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import scrapy
import io


URL_TEMPLATE = 'https://www.tripadvisor.com.au/Attraction_Review-g255103-d526770-r%s.html'
#URL_TEMPLATE = 'https://www.tripadvisor.com.au/Attraction_Review-g255100-d269501-Reviews-or%s-Australian_Centre_for_the_Moving_Image-Melbourne_Victoria.html'

#def url_generator():
#    for page in revID:
#        yield URL_TEMPLATE % (revID)

with io.open('reviewID.txt', 'rt') as f:
    reviewIDs = [url.strip() for url in f.readlines()]

class TripAdvisorReview(scrapy.Spider):
    name = "tripadvisor"
    start_urls = reviewIDs

    def parse(self, response):
        for review in response.css('.reviewSelector'):
            id = review.css('::attr(id)').extract_first()
            if id.startswith("review_title"):
                continue

            yield {
                'id': id.replace("review_", ""),
		'date': review.css('.ratingDate ::attr(title)').extract_first(),
                'title': review.css('.quote ::text').extract_first(),
                'body': review.css('.partial_entry ::text').extract_first(),
                'rating': int(review.css('.rating   .ui_bubble_rating ::attr(class)').re(r'ui_bubble_rating bubble_(\d\d)')[0])/10.0,
            }


