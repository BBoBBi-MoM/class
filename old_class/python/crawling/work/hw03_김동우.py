#%%
import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/sise_market_sum.naver'
html = requests.get(URL)
soup = BeautifulSoup(html.text,'html.parser')

FRONT_URL = 'https://finance.naver.com'
company_list = list()
td_list = soup.select('td>a[href]')
for idx in range(20):
    link = td_list[idx]['href']
    if td_list[idx].text == '':
        continue
    company_list.append([td_list[idx].text,FRONT_URL+link])

class StockTopTen:
    def __init__(self,company_list):
        self.company_list = company_list
        for idx in range(10):
            print(f'[ {idx+1}] {self.company_list[idx][0]}')
        input_value = int(input('주가를 검색할 기업의 번호를 입력하세요(-1:종료):'))
        if input_value == -1:
            return
        elif 0<input_value<11:
            return self.show_information(input_value)
        else:
            print('잘못된 입력입니다.')
            return self.__init__(self.company_list)
    
    def show_information(self,input_value):
        url = self.company_list[input_value-1][1]
        print(url)

        html = requests.get(url)
        soup = BeautifulSoup(html.text,'html.parser')
        blind = soup.select('span.blind')
        price_list =list()
        for row in blind:
            price_list.append(row.text)

        print('종목명:',soup.select_one('title').text[:-9])
        print('종목코드:',soup.select_one('span.code').text)
        print('현재가:',price_list[-10])
        print('전일가:',price_list[-7])
        print('시가:',price_list[-3])
        print('고가',price_list[-6])
        print('저가:',price_list[-2])
        return self.__init__(self.company_list)

test=StockTopTen(company_list)

