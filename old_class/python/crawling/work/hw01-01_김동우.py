#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY'
html1 = urlopen(URL)
soup = BeautifulSoup(html1.read(),'html.parser')

def scraping_use_find(html):
    print('[find 함수 사용]')
    print('-'*45)   
    li_tags=soup.find_all('li',{'class':'forecast-tombstone'})

    print('총 tombstone-container 검색 개수:',len(li_tags))
    print('-'*45)

    for li in li_tags:
        print('[Period]',li.find('p',{'class':['period-name']}).text)
        print('[Short desc]',li.find('p',{'class':['short-desc']}).text)
        print('[Temperature]',li.find('p',{'class':['temp']}).text)
        print('[Image desc]',li.find('img')['title'])
        print('-'*45)

def scraping_use_select(html):
    print('[select 함수 사용]')
    print('-'*45)
    li_tags = soup.select('li.forecast-tombstone')

    print('총 tombstone-container 검색 개수:',len(li_tags))
    print('-'*45)

    for li in li_tags:

        print('[Period]',li.select_one('p.period-name').text)
        print('[Short desc]',li.select_one('p.short-desc').text)
        print('[Temperature]',li.select_one('p.temp').text)

        print('[Image desc]',li.select_one('img')['title'])
        print('-'*45)        
scraping_use_find(html1)
print('\n'*5)
scraping_use_select(html1)




# %%
