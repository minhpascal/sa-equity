import openpyxl
import get_ticker_info 
import filter_bullets
import string 
import glob
import csv
import os
import collections


class TickerInfo(object):
    def __init__(self,tag,ticker): #single ticker
        self.ticker = ticker.upper()
        self.tag = tag
        Scraper = get_ticker_info.GetTickerInfo(self.tag,self.ticker)
        self.text = Scraper() 

        
    def get_attr_at_date(self, **date):
        '''
        year/day/month values of date most be ints
        '''
        res = list()
        for key,value in self.text.items():
            #Python shortcircuits boolean exprs; no KeyError
            is_day,is_month,is_year = [True]*3
            if 'year' in date.keys():
                is_year = date['year'] == key.year
            if 'month' in date.keys():
                is_month = date['month'] == key.month
            if 'day' in date.keys():
                is_day = date['day']== key.day
            if (is_year and is_month and is_day):
                res.append(value)
        return res

    @property
    def summarized(self):
        return {key : filter_bullets.filter_event_frame(self.text[key]) for key in self.text}
        #self.text[key] is a list of strings
    def search(self,term,interval=None):
        '''
        assumes interval is tuple of datetime.date objects
        '''
        result = collections.defaultdict(collections.deque())
        for date,frame in self.texts.items():
            for bullet in frame:
                if term in bullet:
                    result[date].append(term)
        if interval is not None:
            start,end=interval
            return {key: result[key] for key in result if (key>start and key<end)}
        else:
            return result


 







 


