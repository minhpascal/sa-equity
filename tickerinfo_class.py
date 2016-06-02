# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:24:35 2016

@author: VineetA
"""

import extract_ma_info

class TickerInfo(object):
    def __init__(self,ticker): #single ticker
        self.ticker = ticker
        self.ma = extract_ma_info.getMAinfo(ticker)
        
    @classmethod
    def get_attr_at_date(self, datekey_ht, **date):
        '''
        year/day/month values of date most be ints
        '''
        res = list()
        for key,value in datekey_ht.items():
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

     

if __name__=='__main__':
    tickers = ['XOM']
    
    ''',
                 'CHK',
                 'SWN',
                 'APC',
                 'COG',
                 'BP',
                 'COP',
                 'EQT',
                 'CVX',
                 'AR',
                 'BHP',
                 'RRC',
                 'EOG',
                 'DVN']'''
    
    tk = list()
    for ticker in tickers:
        tk.append(TickerInfo(ticker))
    