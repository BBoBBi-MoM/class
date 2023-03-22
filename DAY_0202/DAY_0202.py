#%%
import csv
f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
print(header)
i = 1
for row in data:
    print(row)
    if i > 5:
        break
    i += 1
f.close()
# %%
import csv
f = open('subwayfee.csv',encoding='utf-8-sig')
data = csv.reader(f)
next(data)
max_rate = 0
rate = 0
for row in data:
    for i in range(4,8):
        row[i] = int(row[i]) # 4, 5, 6, 7 컬럼값을 정수로 변환
    rate = row[4] / row[6] # [6]컬럼의 값이 0인 행 확인 용도
    if rate > max_rate:
        max_rate = rate

print(max_rate)
#%%
import csv
f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
rate = 0
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i]) # 4, 5, 6, 7 컬럼값을 정수로 변환
    
    rate = row[4] / (row[4] + row[6])
    if row[6] == 0: # 무임승차 인원[6]이 없는 역 출력
        print(row)

f.close()
#%%
import csv
f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate =0
rate = 0
i = 0
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i]) # 4, 5, 6, 7 컬럼값을 정수로 변환
    if row[6] != 0:
        # 무임 승차 (%) = (무임 승차 수 x 100) / (유임 승차 수 + 무임 승차 수)
        rate = (row[6] * 100) / (row[4] + row[6])
        if rate > max_rate:
            max_rate = rate
            print(row, round(rate, 2), '%')

f.close()
#%%
import csv
f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
max_rate = 0
rate = 0
max_row = []
total_count = 0
max_total_num = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    total_count = row[4] + row[6] # 유임승차수 + 무임승차수
    if (row[6] !=0) and (total_count >100000) :
        rate = row[4] / total_count
        if rate > max_rate :
            max_rate = rate
            max_row = row
            max_total_num = total_count
#%%
import matplotlib.pyplot as plt
plt.pie([10, 20])
plt.show()

#%%
import matplotlib.pyplot as plt
import platform
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else: # MacOS: ‘Darwin’
    plt.rc('font', family='AppleGothic')
numbers = [214, 2312, 1031, 1233]
blood_type = ['A형', 'B형', 'AB형', 'O형']
plt.axis('equal') # 파이 차트를 원형으로 그려줌
plt.pie(numbers, labels=blood_type, autopct='%.1f%%')
plt.legend()
plt.show()