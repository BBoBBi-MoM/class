from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import time
start_time = time()
new_csv=open('./hollys_branches.csv','w',encoding='utf-8')
column_list = ['매장이름','위치(시,구)','주소','전화번호']
new_csv.write(f'"{column_list[0]}","{column_list[1]}","{column_list[2]}","{column_list[3]}"\n')

num=1

for i in range(1,54):
    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
    html = urlopen(url)
    soup = BeautifulSoup(html.read(),'html.parser')
    table = soup.select_one('tbody')
    rows = table.select('tr')
    for row in rows:
        values = row.text.split('\n')
        print(f'[{num}]:매장이름:{values[3]}, 지역:{values[2]}, 주소:{values[5]}, 전화번호:{values[-2]}')
        new_csv.write(f'"{values[3]}","{values[2]}","{values[5]}","{values[-2]}"\n')
        num+=1
    html.close()
new_csv.close()
end_time = time()
print(end_time-start_time)
#16.691338539123535