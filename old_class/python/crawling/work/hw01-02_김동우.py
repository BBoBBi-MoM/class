#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8'
naver_html = urlopen(url)
url = 'https://search.naver.com/search.naver?query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8'
html = urlopen(url)
def get_naver_weather(html):
    soup = BeautifulSoup(html.read(),'html.parser')
    title = soup.select_one('div.title_area > h2.title').text
    weather_info = soup.select_one('div.temperature_text').text
    weather_before_slash = soup.select_one('span.weather').text
    today_conditions = soup.select_one('ul.today_chart_list')
    print(title)
    print(weather_info)
    print(weather_before_slash)
    for i in range(4):
        title = today_conditions.select('strong')[i].text
        content = today_conditions.select('span')[i].text
        print(f'{title} {content}')

    hourly_weather = soup.select_one('div.graph_inner')
    info_list = hourly_weather.select('span.blind')
    time_list = hourly_weather.select('em')
    temperature_list = hourly_weather.select('span.num')
    print('-'*45)
    print('시간대별 날씨 및 온도')
    print('-'*45)
    for i in range(len(info_list)):
        info = info_list[i].text
        time = time_list[i].text
        temperature = temperature_list[i].text
        print(time.ljust(7), end='')
        print(info.ljust(5-len(info)), end=' ')
        print(temperature.rjust(5))
get_naver_weather(naver_html)
# %%
