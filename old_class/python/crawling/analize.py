#%%
import pandas as pd
#%%
ai_df = pd.read_csv(r'./ai_job_info(lastest).csv')

ai_pay=ai_df[ai_df.iloc[:,-1]!='None']
ai_pay_mean = ai_pay.iloc[:,-1].astype('int').mean()
ai_pay_mean = round(ai_pay_mean,0)
# %%
ds_df = pd.read_csv(r'./ds_job_info(lastest).csv')

ds_pay=ds_df[ds_df.iloc[:,-1]!='None']
ds_pay_mean = ds_pay.iloc[:,-1].astype('int').mean()
ds_pay_mean = round(ds_pay_mean,0)
# %%
netflix_inform=ds_df[ds_df['company'].str.contains('Netflix')]
print(netflix_inform)
# %%
nvidia_inform=ds_df[ds_df['company'].str.contains('NVIDIA')]
print(netflix_inform)
# %%
google_inform=ai_df[ai_df['company'].str.contains('NVIDIA')]

# %%
imp