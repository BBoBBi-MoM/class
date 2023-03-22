'''
시프트 + 엔터 누르면 주피터 커널로 실행됩니다..
'''
#%%
import pandas as pd
import matplotlib.pyplot as plt
import platform

df = pd.read_csv('daegu-utf8.csv')
df['날짜'] = pd.to_datetime(df['날짜'])

def temperature():
    start_year = int(input('시작연도를 입력하시오:'))
    end_year = int(input('마지막 연도를 입력하시오:'))
    target_month = int(input('기온 변화를 측정할 달을 입력하시오:'))

    target_df = df[df['날짜'].dt.year >=start_year]
    target_df = target_df[target_df['날짜'].dt.year <=end_year]
    target_df = target_df[target_df['날짜'].dt.month == target_month]
    target_df = target_df.groupby(by=target_df['날짜'].dt.year).mean()
    print(f'{start_year}년부터 {end_year}년까지 {target_month}월의 기온 변화')

    print(target_month,'월 최저기온 평균:')
    for idx in range(len(target_df)):
        print(round(target_df.iloc[idx,-2],1),end='  ')
    print('')

    print(target_month,'월 최저기온 평균:')
    for idx in range(len(target_df)):
        print(round(target_df.iloc[idx,-1],1),end='  ')

    plt.figure(figsize=(20,4))
    plt.title(f'{start_year}년부터 {end_year}년까지 {target_month}월의 기온 변화')
    plt.xticks(range(start_year,end_year+1))
    plt.plot(target_df.iloc[:,-2],color='blue',marker='s',label='최저기온')
    plt.plot(target_df.iloc[:,-1],color='red',marker='o',label='최고기온')
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic', size=8)
    else:
        plt.rc('font', family='AppleGothic', size=8)
    plt.rcParams['axes.unicode_minus'] = False
    plt.legend(loc=2)
    plt.show()

temperature()

# %%
