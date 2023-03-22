#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')
table_tag = soup.find('table', {'id':'giftList'})
table_tag = soup.select_one('table#giftList')
for child in table_tag.children:
    print(child)
# %%
desc = soup.select_one('table#giftList').descendants
print(len(list(desc)))
# %%
for child in soup.select_one('table#giftList').descendants:
    print(child)
#%%
for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

# %%
for sibling in soup.select_one('table#giftList').tr.next_siblings:
    print(sibling)
# %%
