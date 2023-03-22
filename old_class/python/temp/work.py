#%%
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from selenium import webdriver
f = open('./link.csv','w',encoding='utf-8')
f.write('"keyword","link"\n')
driver = webdriver.Chrome('./chromedriver.exe')
ROOT_URL =r'https://search.career.co.kr/jobs?kw='

keyword_list = ['AI','머신러닝','인공지능','빅데이터','딥러닝']
for keyword in keyword_list:
    url = ROOT_URL+keyword
    driver.get(url)
    for idx in range(2,10):
        html=driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        link_list = soup.select('a.tx')
        for link in link_list[::-2]:
            link= link['href']
            f.write(f'"{keyword}","{link}"\n')
        try:
            driver.execute_script(f'javascript:goList({idx})')
        except:
            continue
f.close()
# %%
