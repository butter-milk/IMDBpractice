from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen
from urllib.request import urljoin
import re

import ssl
data = dict()

regex = re.compile('\>(.*?)\<')
def scrape(page):
    primaryKey = (page-1)*800
    webpage = "https://quotes.toscrape.com/page/"+str(page)+ "/"
    webpageHTML = ""
    try:
        webpageHTML = urlopen(webpage, context=ssl.SSLContext()).read()
    except:
        print("Error like wtf")
        return
    page_soup = soup(webpageHTML, "html.parser")
    quotes = page_soup.findAll("div", {"class":"quote"})
    for quote in quotes:
        tags = quote.findAll("a", {"class":"tag"})
        text = re.search(r'\“(.*?)\”',str(quote.findAll("span", {"class":"text"})[0])).group(1)
        text.replace("\"","\'")
        author = regex.search(str(quote.findAll("small", {"class":"author"})[0])).group(1)
        for tag in tags:
            t = regex.search(str(tag)).group(1).replace('-','').replace('read','READZ').replace('value','VALUEZ').replace("\"","\'")

            if t not in data.keys():
                data[t] = []
            data[t].append(  (primaryKey, author,text)  )
        primaryKey+=1
def main(pages):
    for i in range(1,pages):
        scrape(i)
    return data
