#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
#%%
URL = 'https://www.pythonscraping.com/pages/warandpeace.html'
html = urlopen(URL)
soup = BeautifulSoup(html.read(),'html.parser')
#%%
object_tag = soup.find('span')
print('object_tag:',object_tag)
print('attrs:',object_tag.attrs)
print('value:',object_tag.attrs['class'])
print('text:',object_tag.text)
 
 #%%
name_list = soup.select('span.green')
# %%
for name in name_list:
    print(name.text)
# %%
prince_list = soup.find_all(text='the prince')
# %%
print(prince_list)

# %%
