#%%
import os
from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup
#%%
download_directory = 'downloaded'
base_url = 'https://pythonscraping.com'

def get_absolute_url(base_url,source):
    if source.startswith('https://www.'):
        url = f'https://{source[11:]}'
    elif source.startwith('http://'):
        url = source
    elif source.startswith('www.'):
        url