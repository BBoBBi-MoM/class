#%%
import pandas as pd
import platform
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
#%%
system_name = platform.system()
if system_name == 'Windows':
# Windows 운영체제
    print('Windows OS')
    plt.rc('font', family='Malgun Gothic')
elif system_name == 'Darwin': # Mac OS
    print('Mac OS')
    plt.rc('font', family='AppleGothic')
elif system_name == 'Linux': # Linux
    print('Linux OS')
    path = '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'
    font_name = fm.FontProperties(fname=path, size=12)
    plt.rc('font', family=font_name)
else:
    print("Not support")
#%%
subway_df = pd.read_csv('subwaytime.csv')
# %%
subway_df = subway_df.iloc[:,[1,3,11,13]]
subway_df = subway_df.iloc[1:,:]
subway_df.iloc[:,[2,3]]=subway_df.iloc[:,[2,3]].astype('int32')
sum_df = subway_df.iloc[:,-2]+subway_df.iloc[:,-1]
subway_df = subway_df.iloc[:,[0,1]]
#%%
subway_df =pd.concat([subway_df,sum_df],axis=1)
# %%
info_dict = dict()
for idx in range(1,8):
    tmp = subway_df[subway_df['호선명']==f'{idx}호선']
    max_row = tmp[tmp[0]==tmp[0].max()]

    line = max_row.iloc[0,0]
    station = max_row.iloc[0,1]
    population = max_row.iloc[0,2]
    
    info_dict[f'{idx}호선 {station}']= population
    print(f'출근 시간대 {line} 최대 하차역: {station}역, 하차인원:{str(population)[:-3]},{str(population)[-3:]}명')
#%%

plt.bar(info_dict.keys(),info_dict.values())
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.xticks(rotation=45)
plt.show()
# %%
subway_df2 = pd.read_csv('subwaytime.csv')
subway_df2 = subway_df2.iloc[1:,[3,11,13]]
sum_df2 = subway_df2.iloc[:,-1].astype('int32') + subway_df2.iloc[:,-2].astype('int32')
station_df = subway_df2.iloc[:,0]
subway_df2 = pd.concat([station_df,sum_df2],axis=1)
subway_df2 = subway_df2.groupby(by='지하철역').sum()
#%%
subway_df2 = subway_df2.sort_values(by=0,ascending=False)
#%%
subway_df2 = subway_df2.head()
#%%
info_dict2 = dict()
for i in range(len(subway_df2)):
    station = subway_df2.index[i]
    population = subway_df2.iloc[i,:][0]
    info_dict2[f'{station}'] = population
    print(f'{station}:{str(population)[:-3]},{str(population)[-3:]}')
plt.bar(info_dict2.keys(),info_dict2.values(),color='blue')
plt.title('서울 지하철 출근시간대 하차 인원 비교(7:00~8:59)')
plt.show()
# %%
