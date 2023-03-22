#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
#%%
#random.seed(datetime.datetime.now())
random.seed(None) # Python 3.9 이상
def get_links(article_url):
    html = urlopen('https://en.wikipedia.org' + article_url)
    bs = BeautifulSoup(html, 'html.parser')
    body_content = bs.find('div', {'id': 'bodyContent'})
    wiki_url = body_content.find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))
    return wiki_url
links = get_links('/wiki/Kevin_Bacon')
print('links 길이: ', len(links))
while(len(links)) > 0:
    new_article = links[random.randint(0, len(links)-1)].attrs['href']
    print(new_article)
    links = get_links(new_article)
# %%
pages = set()
count = 0
def get_links(page_url):
    global pages
    html = urlopen(f'https://en.wikipedia.org{page_url}')
    bs = BeautifulSoup(html.read(),'html.parser')
    for link in bs.select('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                new_page = link.attrs['href']

                count += 1
                print(f'[{count}]:{new_page}')
                pages.add(new_page)
                get_links(new_page)
get_links('')

# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set() # 세트 선언
count = 0
def getLinks(pageUrl):
    global pages,count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:

                newPage = link.attrs['href']
                count += 1
                print('[{0}]: {1}'.format(count, newPage))
                pages.add(newPage)
                getLinks(newPage)
               
getLinks('')
# %%
