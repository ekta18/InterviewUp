#import library
import requests
from bs4 import BeautifulSoup
import pandas as pd

#enter URL
url = "http://feeds2.feedburner.com/sitechnews"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

soup.prettify()

items = soup.findAll('item')

item = items[1]

news_items = []

for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    #news_item['pubDate'] = item.pubDate.text
    news_items.append(news_item)
    
df = pd.DataFrame(news_items,columns=['title','description'])

print(df)


#ekta this step below is optional to store results in csv file
df.to_csv('data1.csv',index=False, encoding = 'utf-8')





#this code is for startups as well, so if u want it use it 
#STARTUPS
url = "http://feeds2.feedburner.com/sivcnews"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

soup.prettify()

items = soup.findAll('item')

item = items[1]

news_items = []

for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    #news_item['pubDate'] = item.pubDate.text
    news_items.append(news_item)
    
df = pd.DataFrame(news_items,columns=['title','description'])

print(df)