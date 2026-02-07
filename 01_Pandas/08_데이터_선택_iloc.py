# iloc : integer loc 를 뜻하며, 정수를 이용해서 DataFrame의 값을 가져오는 것임.

import pandas as pd

df = pd.read_excel('hello.xlsx', index_col='지원번호')
# print(df)

a = df.iloc[0] # index 0인 행의 모든 Data들을 가져옴
print(a)

b = df.iloc[5] # index 5인 행의 모든 Data들을 가져옴
print(b)

c = df.iloc[0:5] # index가 0-4 인 행의 모든 Data들을 가져옴
print(c)

d = df.iloc[0,1] # 0번째 위치와 1번째(학교) 데이터 
print(d)

e = df.iloc[2:6, 1]
print(e)

f = df.iloc[1:3, 0:5]
print(f)
