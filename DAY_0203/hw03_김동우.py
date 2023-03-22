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
df = pd.read_csv('./gender.csv',thousands = ',')
df = df.iloc[:,[0,14,27]]
deagu_df1 = df[df['행정구역'].str.contains('대구광역시 중구')]
deagu_sr1= deagu_df1.iloc[0,:]
deagu_df2 = df[df['행정구역'].str.contains('대구광역시 동구')]
deagu_sr2= deagu_df2.iloc[0,:]
deagu_df3 = df[df['행정구역'].str.contains('대구광역시 서구')]
deagu_sr3= deagu_df3.iloc[0,:]
deagu_df4 = df[df['행정구역'].str.contains('대구광역시 남구')]
deagu_sr4= deagu_df4.iloc[0,:]
deagu_df5 = df[df['행정구역'].str.contains('대구광역시 북구')]
deagu_sr5= deagu_df5.iloc[0,:]
deagu_df6 = df[df['행정구역'].str.contains('대구광역시 수성구')]
deagu_sr6= deagu_df6.iloc[0,:]
deagu_df7 = df[df['행정구역'].str.contains('대구광역시 달서구')]
deagu_sr7= deagu_df7.iloc[0,:]
deagu_df8 = df[df['행정구역'].str.contains('대구광역시')]
deagu_sr8= deagu_df8.iloc[0,:]
plt.figure(figsize=(12,6))
for iter in range(8):
        plt.subplot(int(f'24{iter+1}'))
        sr = globals()[f'deagu_sr{iter+1}']
        plt.title(sr[0][:-13])
        plt.pie(sr[1:],labels=['남성','여성'],autopct='%.1f%%',startangle=90)
plt.show()
# %%
dict_city_a = {'0-9': 80, '10-19': 100,'20-9': 140,'30-39': 160,'40-49': 200,
              '50-59': 240,'60-69': 195,'70-79': 160,'80-89': 80,'90-99': 20} 
dict_city_b = {'0-9': 120, '10-19': 200,'20-29': 300,'30-39': 360,'40-49': 400,
              '50-59':300,'60-69': 40,'70-79': 25,'80-89': 20,'90-99': 10 }

#%% (1)
city_key_list = list(dict_city_a.keys())
city_a_values = list(dict_city_a.values())
city_b_values = list(dict_city_b.values())
#%%
def draw_barchart(key_list,value_list1,value_list2):
    x0 = list(range(10))
    x1 = [(x-0.2) for x in range(10)]
    x2 = [(x+0.2) for x in range(10)]
    plt.figure()
    
    plt.title('The demographics of two cities')
    plt.xlabel('age')
    plt.ylabel('Population')

    plt.bar(x1,value_list1,width=0.4)
    plt.bar(x2,value_list2,width=0.4)
    plt.xticks(x0,key_list)
    plt.legend(['City A' ,'City B'])
    plt.savefig('barchart01.png', dpi=100)
    
    plt.show()
draw_barchart(city_key_list,city_a_values,city_b_values)
#%%
city_a_total = sum(city_a_values)
city_b_total = sum(city_b_values)
voting_pop_a = sum(city_a_values[2:])
voting_pop_b = sum(city_b_values[2:])
old_pop_a = sum(city_a_values[-3:])
old_pop_b = sum(city_b_values[-3:])
#%%
def draw_piechart(total1,value1,total2,value2,title_name):
    rate_a1 = value1/total1
    rate_a2 = (total1-value1)/total1
    rate_b1 = value2/total2
    rate_b2 = (total2-value2)/total2
    plt.figure(figsize=(8,6))
    plt.subplot(1,2,1)
    plt.title(f'city A\'s {title_name}')
    plt.pie([rate_a1,rate_a2],autopct='%.1f%%',labels=[f'{title_name}',''])
    plt.subplot(1,2,2)
    plt.title(f'city B\'s {title_name}')
    plt.pie([rate_b1,rate_b2],autopct='%.1f%%',labels=[f'{title_name}',''])
    plt.savefig(f'./{title_name}.png', dpi=100)    
    plt.show()
# %%
draw_piechart(city_a_total,voting_pop_a,city_b_total,voting_pop_b,title_name="Voting rate")
# %%
draw_piechart(city_a_total,old_pop_a,city_b_total,old_pop_b,title_name="old rate")
# %%
