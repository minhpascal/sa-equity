
import tickerinfo_class as tk
#import openpyxl
import pandas

class SeekingAlphaCursor(object):
    def __init__(self):
        with open("tickers.txt") as f:
            target_str = f.read()
        self.tickers = [word.strip() for word in target_str.split(',')]
        self.TickerInfos = dict()
        self.end_year,self.start_year = 0
        
        for ticker in self.tickers:
            self.TickerInfos[ticker] = tk.TickerInfo(ticker)
            
        self.df = None
            
  
    def write_all_to_excel(self,path):
        '''
        ws = openpyxl.Workbook()
        for i in range(1,2+(self.end_year-self.start_year)):
            ws.active.cell(row=1, column = i+1).value = self.end_year+1-i
        for i,e in enumerate(self.tickers):
            ws.active.cell(row = i+2, column = 1).value = e
     
        for i,e in enumerate(tk):
            for j in range(self.start_year,self.end_year+1):
                e.write_to_excel_at_year(ws=ws, year=j,info_ht=e.ma)
        ws.save(path+'sa.xlsx') 
        '''
        if self.df is  None:
            self.write_to_df()
        self.df.to_excel(path+'sa.xlsx', sheet_name = 'output')
        print('See:', path+'sa.xlsx')


    def write_to_df(self):
        self.df = pandas.DataFrame.from_dict(self.TickerInfos, orient ='index')
        return self.df

    
