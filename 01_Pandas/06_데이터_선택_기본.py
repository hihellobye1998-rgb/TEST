# 데이터 선택 (기본)

import pandas as pd

df = pd.read_excel('hello.xlsx', index_col='지원번호')
# print(df)


# 1. Column 선택 (label)

series = df['이름']
print(series)
series2 = df[['이름', '키']]
print(series2)


# # 2. Column 선택 (index)

df.columns

df.columns[0]

df.columns[2]

# 3. 슬라이싱

x = df['영어'][0:3]
print(x)

x = df['수학'][2:]
print(x)

