#%%
import pandas as pd
#%%
raw_table = pd.read_html('https://oekim.tistory.com/79',encoding='utf-8',header=0)[1]
en_kor_table = raw_table.iloc[:-1,[0,1,3]]
# %%
en_kor_table.to_csv('./name_data.csv')
# %%
