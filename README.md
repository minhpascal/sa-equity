Scrape SeekingAlpha pages for M&A, earnings, and news. 
###Installation
1. For now, `git clone https://github.com/vapte/sa-equity.git` will have to do. Plans to register on PyPI in the future.
2. Fill in `resources/keys.yaml `
3. `import equitysa`

###Usage
For one ticker, the `TickerInfo` class is sufficient.

Example: Get M&A news on XOM from May 2014:

```
tk_info = TickerInfo(ticker='xom',tag='ma')
xom_ma_14 = TickerInfo.get_attr_at_date(tk_info.ma, **{'year':2014,'month':5})
```

For multiple tickers, load `tickers.txt` with comma-separated tickers and use theSeekingAlphaCursor interface

Example: Writes summarized M&A news to `data.xlsx`

```
cursor = SeekingAlphaCursor(tag='ma')
cursor.write_all_to_excel('/path/to/data.xlsx',summ=True)
```

Current tag idioms are:
```
	{
		'news':'/news/on-the-move/',
		'ma':'/news/m-a/',
		'dividends': '/news/dividends/',
		'earnings': '/news/earnings_news/',
		'general': '/news/'
	}
```

###License
MIT
