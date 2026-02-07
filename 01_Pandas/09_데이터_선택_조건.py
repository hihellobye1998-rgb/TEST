# 데이터 선택 (조건) : 조건에 해당하는 Data들 가져오는 작업

import pandas as pd

df = pd.read_excel('hello.xlsx', index_col='지원번호')
# print(df)

# 1. 필터링
filter = df['키'] >= 185  # df의 '키' 컬럼에서 185 이상인지 여부를 True, False로 알려줌 
print(df[filter]) # df에서 filter가 True인 data만 보여줘 ! 
print(df[-filter]) # filter를 역으로 사용

df = df[df['키']>=190]
print(df)

df = df.loc[df['키']>=190, '수학'] # 키가 190 이상인 학생들의 수학점수
print(df)


# 2. 다양한 조건 

## 그리고 ( & )
a = df.loc[ (df['키']>=185) & (df['학교'] == '북산고') ]   # ('키'가 185 이상이고) & ('학교'가 북산고인) Data 가져오기 
print(a)

## 또는 ( | )
b = df.loc[ ( df['키']<170 ) | (df['키']>=200) ] # ('키'가 170 미만이거나) | ('키'가 200 이상인 ) Data들 가져오기. 
print(b)

