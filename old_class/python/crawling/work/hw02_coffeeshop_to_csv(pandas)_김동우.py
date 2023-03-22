from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from time import time
start_time = time()
num=1
branch = list()
for i in range(1,54):
    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
    html = urlopen(url)
    soup = BeautifulSoup(html.read(),'html.parser')
    table = soup.select_one('tbody')
    rows = table.select('tr')
    for row in rows:
        values = row.text.split('\n')
        print(f'[{num}]:매장이름:{values[3]}, 지역:{values[2]}, 주소:{values[5]}, 전화번호:{values[-2]}')
        branch.append([values[3],values[2],values[5],values[-2]])
        num+=1
    html.close()

df = pd.DataFrame(branch, columns=['매장이름', '위치(시,구)', '주소', '전화번호'])
df.to_csv('./hollys_branches.csv', encoding='utf-8', mode='w', index=True)
end_time = time()
print(end_time-start_time) #17.3081157207489