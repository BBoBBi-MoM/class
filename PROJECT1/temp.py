#%%
import pandas as pd
import matplotlib.pyplot as plt
import platform
import seaborn as sns
#%%
system_name = platform.system()
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

#%%
rate_df = pd.read_csv('./data/macket_interest.csv',index_col='year')
moneytary_df = pd.read_csv('./data/M1.csv',index_col='year')
gdp_df = pd.read_csv('./data/gdp.csv',thousands=',',index_col='year')
consumer_df = pd.read_csv('./data/consumer_price.csv',index_col='year')
price_df = pd.read_csv('./data/apart_price.csv')
price_df['year'] = price_df.iloc[:,0].astype(int)
price_df = price_df.groupby('year').mean()
consumer_df = round((consumer_df/consumer_df.iloc[-4])*100,2)
moneytary_df = round(moneytary_df/moneytary_df.iloc[-4]*100,2)
total_df = pd.merge(left = moneytary_df , right = gdp_df, how = "inner", on = "year")
total_df = pd.merge(left=total_df, right= rate_df, how = 'inner',on='year')
total_df = pd.merge(left=total_df, right=consumer_df,how='inner',on='year')
total_df = pd.merge(left=total_df,right=price_df,how='inner',on='year')
sub_df = total_df[['M1','real_GDP','price','Korea_rate']]
corr = sub_df.corr()

# %%
scaled_price = total_df.iloc[:,-1]
scaled_price = (scaled_price - scaled_price.min())/(scaled_price.max()-scaled_price.min())
consumer_df = total_df.iloc[:,-2]
korea_rate = total_df.iloc[:,2]
us_rate = total_df.iloc[:,3]
price = total_df.iloc[:,-1]
normal_korea_rate = (korea_rate-korea_rate.mean())/korea_rate.std()
normal_us_rate = (us_rate-us_rate.mean())/us_rate.std()
normal_price = (price - price.mean())/price.std()
price_index = price/price.iloc[-4]*100
m1 = total_df.iloc[:,0]


#%%
plt.plot(korea_rate,label='한국 금리',marker = 'o')
plt.plot(us_rate,label='미국 금리',marker = 'o')
plt.title('한국과 미국의 금리변화')
plt.legend()
plt.ylabel('interest rate')
plt.show()
#%%
plt.plot(korea_rate,label = '금리',marker='o')
plt.plot(scaled_price, label = '아파트 가격',marker='o')
plt.title('금리와 아파트 가격')
plt.legend()
plt.show()

# %%
plt.plot(price_index,label='아파트 가격 지수',marker='o')
plt.plot(consumer_df,label='소비자 물가 지수',marker='o')
plt.legend()
plt.title('소비자 물가 지수, 아파트 가격 지수 비교')
plt.show()
'''경기 침체 - 통화량 증가(양적완화) - 경제 과열,물가 상승 - 금리 인상,'''
# %%
plt.plot(m1,label=' M1 통화량')
plt.plot(consumer_df,label='소비자 물가 지수')

plt.legend()
plt.title('소비자 물가 지수,통화량 비교')
plt.show()
# %%
sns.heatmap(corr,
            cmap='Greys',
            annot = True,
            linewidths = .5,
            fmt = '.2f',
            square = True,
            vmin = -1, vmax= 1)
plt.show()
# %%
