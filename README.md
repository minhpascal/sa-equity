Scrape SeekingAlpha pages for M&A, earnings, and news. 
###Installation
1. For now, `git clone https://github.com/vapte/sa-equity.git` will have to do. Plans to register on PyPI in the future.
2. `import equitysa`

###Usage
The `TickerInfo` class is sa-equity's principal interface. 

Example: Get M&A news on XOM from May 2014:

```
tk_info = TickerInfo(ticker='xom',tag='ma')
xom_ma_14 = TickerInfo.get_attr_at_date(tk_info.ma, **{'year':2014,'month':5})
```
Writing to Excel is a WIP.

###License
MIT
