#%%
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import matplotlib.pyplot as plt
#%%
link_df = pd.read_csv('link.csv')
# %%
for idx in range(len(link_df)):
    link = link_df.iloc[idx,-1]
    html=requests.get(link).content
    soup = BeautifulSoup(html,'html.parser')
    span_list = soup.select('span.vl')
    temp_list = list()
    for span in span_list:
        temp_list.append(span.text)
    
    break
# %%
