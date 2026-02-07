from heapq import nlargest
from numpy import average
import pandas as pd


# excel 파일 열기
df = pd.read_excel('hello.xlsx', index_col='지원번호')
print(df)


print(df.describe()) # Dataframe에서 계산 가능한 데이터에 대해서 Column 별로 데이터의 갯수, 평균, 표준편차, 최소/최대값 등의 정보를 보여줌.
print(df.info()) # df의 정보에 대해서 알 수 있는 메소드 ( 컬럼명, 데이터타입, 개수 )

print(df.head()) # df의 헤드 5개만 요약해서 보는 메소드
print(df.tail()) # df의 마지막 5개만 요약해서 보는 메소드

print(df.values) # df 안의 데이터들이 어떤 값을 가졌는지 한 눈에 볼 수 있는 메소드

print(df.index) # df index에 대한 정보 index 칼럼명 등 알 수 있는 메소드
print(df.columns) # df의 column에 대해 알 수 있는 정보 메소드

print(df.shape) # df의 row, column 개수에 대해 알 수 있느 메소드 (8,9)


# Series 확인

print(df['키']) # Dataframe에서 '키' 라는 컬럼명을 가진 Series 확인

info = df['키'].describe() # df에서 '키'라는 컬럼명에 대한 정보 확인 메소드
min = df['키'].min() # df에서 '키'라는 컬럼명의 최소값
max = df['키'].max()
nnlargest = df['키'].nlargest(3) # 키 큰 사람 순서대로 3명 데이터
aaverage = df['키'].mean() # df에서 '키' 컬럼 데이터의 평균
sum = df['키'].sum() # 키 컬럼명 Series 에서 Data들을 모두 합한 것

unique = df['학교'].unique() # 중복을 제외한 고유한 unique 값들만 가져옴 # 북산고, 능남고
num_unique = df['학교'].nunique() # 중복을 제외하고 고유한 unique 값들이 몇개인지 ? 

print(info)
print(min, max)
print(nnlargest)
print(aaverage)
print(sum)
print(unique)
print(num_unique)
