#%%
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#%%
temp_url = 'https://www.pythonscraping.com/pages/page1.html'
html = urlopen(temp_url)
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs)
#%%
print(bs.title)

# %%
def get_title(url,tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs_object = BeautifulSoup(html.read(),'html.parser')
        value = bs_object.body.find(tag)
    except AttributeError as e:
        return None
    return value

tag = 'h1'
value = get_title(url=temp_url,tag=tag)
if value == None:
    print(f'{tag} could not be found')
else:
    print(value)
# %%
