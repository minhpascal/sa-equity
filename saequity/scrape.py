#scrape.py

import bs4
import requests
import yaml
import re
import calendar 
from datetime import timedelta
from datetime import date

request_header= {"Referer": "http://seekingalpha.com/",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

def is404(html):
    b= bs4.BeautifulSoup(html,'lxml')
    return len(b.findAll('a' , {'href':"/stock-ideas", 'sasource':"error_page_404"}))!=0
    
def loginSA():
    #we get data from keys
    global request_header
    filepath = "resources/keys.yaml"   
    with open(filepath, 'r') as f:
        keys = yaml.load(f)
        #print(keys['username'])
        #print(keys['password'])
        # Start a session so we can have persistent cookies
    sessionRequests = requests.Session()
    

    loginUrl = "http://seekingalpha.com/account/login"

    # This is the form data that the page sends when logging in
    loginData = {
        'slugs[]': None,
        'rt':None,
        'user[url_source]':None,
        'user[location_source]':'orthodox_login',
        'user[email]':keys['username'],
        'user[password]':keys['password']}
    # Authenticate
 
    r = sessionRequests.post(loginUrl, data = loginData, headers=request_header)

    return [r.status_code, sessionRequests]

def getHTML(url):
    global request_header
    status_code, session = loginSA()
    return session.get(url, headers = request_header).text

def parsePage(html):
    page_ht = dict()    #(key,value) = (date, [bullet_1,bullet_2,..,bullet_k])
    blocks = grabNewsBlocks(html)
    for block in blocks:
        page_ht[get_date(block)] = get_bullets(block)
    return page_ht
        

def get_date(block):
    d_raw = block.findAll("span", {'class': 'date pad_on_summaries'})
    d_str = removeInTag(str(d_raw[0]))
    d_list = [x.strip(',.') for x in d_str.split(' ')]
    if ('Today' in d_str):
        return date.today()
    if ('Yesterday' in d_str):
        return date.today() - timedelta(days=1)
    isCurrYear = False
    if (not len(list(filter(lambda x:len(x)==4 and x.isnumeric(), d_list)))==1):
        isCurrYear = True
    if isCurrYear:
        year, month, day =  date.today().year , list(calendar.month_abbr).index(d_list[1]), int(d_list[2])       
    else:
        year, month, day = int(d_list[2]), list(calendar.month_abbr).index(d_list[0]), int(d_list[1])
    return date(year, month,day)
    
def get_bullets(block):
    return [removeInTag(str(bullet)) for bullet in block.findAll("li")]
    
def removeInTag(s):
    cleaner = re.compile('<.*?>')
    cleantext = re.sub(cleaner,'', s)
    return cleantext        
        
def grabNewsBlocks(html):   #pulls the bullet blocks from a page
    bullet_header = "mc_list_texting right bullets"
    b = bs4.BeautifulSoup(html,'lxml')
    return b.findAll("div", {"class":bullet_header})

