# 데이터 선택 (loc) : 이름을 이용하여 원하는 row에서 원하는 col 선택

import pandas as pd

df = pd.read_excel('hello - 복사본.xlsx', index_col = '지원번호')
# print(df)

a = df.loc['3번'] # index가 '3번'인 data 행의 전체 데이터를 모두 가져옴
print(a)

b = df.loc['3번', '국어'] # index가 '3번'인 행의 data 중 '국어'의 칼럼을 가져옴
print(b)   # 40

c = df.loc[['3번', '5번'], '국어'] # index가 '3번', '5번'인 data 행의 '국어' 칼럼을 가져옴 
print(c)   # 3번 40, 5번 80 Series 형식

d = df.loc[['1번','3번'], ['영어', '국어']] 
print(d)

e = df.loc['1번':'5번', '국어':'사회']  # index가 '1번' ~ '5번' 에서 칼럼이 '국어' ~ '사회' 까지 Data 가져오기
print(e)

