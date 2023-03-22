#%%
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from selenium import webdriver
import time
import pandas as pd
#%%
SEARCH_URL = r'https://www.simplyhired.com/search?q=AI&pn='
ROOT_URL = r'https://www.simplyhired.com'
f = open('./AI_link.csv','w')
f.write('"link"\n')
for i in range(1,92):
    print(i)
    url = SEARCH_URL+str(i)
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    link_list=soup.select('a.SerpJob-link')
    
    for link in link_list:
        link = link['href']
        f.write(f'{ROOT_URL+link}\n')
f.close()

# # %%
# SEARCH_URL = r'https://www.simplyhired.com/search?q=data+scientist&pn='
# ROOT_URL = r'https://www.simplyhired.com'
# f = open('./data_scientist_link.csv','w')
# f.write('"link"\n')
# for i in range(1,92):
#     print(i)
#     url = SEARCH_URL+str(i)
#     html = requests.get(url).content
#     soup = BeautifulSoup(html,'html.parser')
#     link_list=soup.select('a.SerpJob-link')
    
#     for link in link_list:
#         link = link['href']
#         f.write(f'{ROOT_URL+link}\n')
# f.close()
# %%
ai_job_info = open('ai_job_info.csv','w',encoding='utf-8')
ai_job_info.write('"company","score","location","salary"\n')
ai_link_df = pd.read_csv('AI_link.csv')
ai_dict = dict()
#%%
#ds_job_info = open('ds_job_info.csv','w',encoding='utf-8')
#ds_job_info.write('"company","score","location","salary"\n')
#ds_link_df = pd.read_csv('data_scientist_link.csv')

#ds_dict = dict()
#%%
for idx in range(1000):
    print(idx)
    url = ai_link_df.iloc[idx,0]
    time.sleep(1.1)
    html = urlopen(url)
    soup = BeautifulSoup(html.read(),'html.parser')
    # try:
    #     company_info=soup.select('div.viewjob-labelWithIcon')[0].text
    #     company_name = company_info.split('-')[0]
    #     score = company_info.split('-')[1]
    #     location = soup.select('div.viewjob-labelWithIcon')[1].text.split(' ')[-1]
    # except:
    #     continue
    
    # try:
    #     salary_info = soup.select_one('span.viewjob-salary').text.split(' ')
    # except:
    #     salary = None
    # if salary_info[-1] == 'year':
    #     try:
    #         max_salary = salary_info[-3].replace(',','').replace('$','')
    #         min_salary = salary_info[-5].replace(',','').replace('$','')
    #         salary = (int(max_salary)+int(min_salary))//2
    #     except:
    #         salary = int(salary_info[0].replace(',','').replace('$',''))
    
        
    # else:
    #     salary = None
    
    # try:
    #     ai_job_info.write(f'"{company_name}","{float(score)}","{location}","{salary}"\n')
    # except:
    #     ai_job_info.write(f'"{company_name}","","{location}","{salary}"\n')

    qualifiction = soup.select('li.viewjob-qualification')
    for word in qualifiction:
        if word.text not in ai_dict:
            ai_dict[word.text] = 1
        else:
            ai_dict[word.text] +=1

#%% 
ai_job_info.close()
# ai_job_info.close()
# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wc = WordCloud(background_color="white",width=1000,height=1000, max_words=10,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(ai_dict)
plt.figure(figsize=(15,15))
plt.imshow(wc)
plt.show()
# %%
