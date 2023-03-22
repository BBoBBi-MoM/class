#%%
from urllib.request import urlretrieve,urlopen
from bs4 import BeautifulSoup
#%%
URL = 'http://www.pythonscraping.com'
html = urlopen(URL)
bs = BeautifulSoup(html,'html.parser')
home_image = bs.select_one('img.pagelayer-img')
image_location = home_image['src']

print(image_location)
urlretrieve(image_location,'logo.jpg')
# %%
download_list = bs.find_all(src=True)
for down_url in download_list:
    print(down_url['src'])
# %%
