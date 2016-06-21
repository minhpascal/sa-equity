
import scrape

class GetTickerInfo(object):
    
    def __init__(self,tag,ticker):
        self.tag = tag
        self.ticker = ticker.upper()

    def __call__(self):
        '''
        pull M&A/writedown data and structure into bullets
        '''
        page = 1
        url = 'http://seekingalpha.com/symbol/'+self.ticker+self.tag+str(page)
        block_ht = dict()
        ma_html = scrape.getHTML(url)
        block_ht.update(scrape.parsePage(ma_html))
        while (True):
            try:    
                ma_html = scrape.getHTML(url)
                if scrape.is404(ma_html):
                    break
                block_ht.update(scrape.parsePage(ma_html))
                page+=1
                url = 'http://seekingalpha.com/symbol/'+self.ticker+self.tag+str(page)
            except:
                break
        print(page-1,"pages parsed for", self.ticker)
        return block_ht    

    

    















    
