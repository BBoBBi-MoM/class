#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#%%
html = urlopen(r'https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.read(),'html.parser')

# for link in bs.select('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
# %%
body_content = bs.select_one('div#bodyContent')
pattern = '^(/wiki/)((?!:).)*$'
for link in body_content.select('a',href = re.compile(pattern)):
    if 'href' in link.attrs:
        print(link.attrs['href'])
# %%
