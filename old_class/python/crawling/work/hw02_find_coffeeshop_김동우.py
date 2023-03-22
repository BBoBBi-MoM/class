#%%
import pandas as pd
import re
#%%
class FindCoffeeshop:
    def __init__(self,path):
        self.df = pd.read_csv(path)
        return self._input()
    
    def _input(self):
        input_value = input('검색할 매장의 도시를 입력하세요:')
        print("-"*30)
        if input_value =='quit':
            return
        else:
            return self._find(input_value)

    def _find(self,input):
        self.temp_df = self.df[self.df['위치(시,구)'].str.contains(input)]
        print('검색된 매장 수:',len(self.temp_df))
        print("-"*30)
        for idx in range(len(self.temp_df)):
            temp_list = list(self.temp_df.iloc[idx])
            print(f'[{idx+1}]:{temp_list[-2:]}')
        print('-'*60)
        return self._input()


        


test=FindCoffeeshop(r'C:\Users\Administrator\Desktop\python\crawling\work\data\hollys_branches1.csv')

