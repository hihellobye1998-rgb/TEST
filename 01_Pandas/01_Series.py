
# Pandas : 파이썬에서 사용하는 데이터 분석 라이브러리
import pandas as pd

# 1. Series 1차원 데이터 (정수, 실수, 문자열)
# # 예) 1월부터 4월까지 평균 온도 데이터 (-20, -10, 10, 20)
temp = pd.Series([-20,-10,10,20]) # 기본적으로 index가 깔림
print(temp[0])  

# 2. Series 객체 생성 (Index 지정)

temp = pd.Series([-20,-10,10,20], index = ['Jan', 'Feb', 'Mar', 'Apr'])
print(temp) # 출력시 테이블형태로 나옴
print(temp['Apr']) # index가 Apr 인 data 출력
print(temp['Jan']) # index가 Jan 인 data 출력