
import tickerinfo_class as tk
import pandas

class SeekingAlphaCursor(object):
    def __init__(self,tag='news'):
        with open("resources/tickers.txt") as f:
            target_str = f.read()
        self.tickers = [word.strip() for word in target_str.split(',')]
        self.TickerInfos = dict()
        self.end_year,self.start_year = 0,0
        self._tag = tag
        
        for ticker in self.tickers:
            self.TickerInfos[ticker] = tk.TickerInfo(ticker =ticker,tag = self.tag)
        
        self.texts = dict()
        for ticker in self.tickers:
            self.texts[ticker] = self.TickerInfos[ticker].text
        self.df = None
            
    @property 
    def tag(self):
        idioms=  {'news':'/news/on-the-move/',
                  'ma':'/news/m-a/',
                  'dividends': '/news/dividends/',
                  'earnings': '/news/earnings_news/',
                  'general': '/news/',
                  }
        if idioms.get(self._tag,None) is not None:
            return idioms[self._tag]
        else:
            return self._tag

    def write_all_to_excel(self,path):
        if self.df is  None:
            self.write_to_df()
        self.df.to_excel(path+'sa.xlsx', sheet_name = 'output')
        print('See:', path+'sa.xlsx')

    @property
    def df(self):
        pandas.DataFrame.from_dict(self.texts, orient ='index')
        

    
