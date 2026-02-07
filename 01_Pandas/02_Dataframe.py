# DataFrame : 2차원 데이터 (Series들의 모음)
## Data 준비 사전 (dict) 자료구조를 통해 생성
## 예) 슬램덩크 주요 인물 8명에 대한 데이터

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
print(data) # 있는 그대로 줄줄이 출력됨





# 1. Data Frame 객체 생성

import pandas as pd

df = pd.DataFrame(data) # pd 라이브러리 안에 DataFrame이라는 메소드를 써서 DataFrame을 만든다. (data)를 통해서.
print(df) # df는 dictonary인 data를 바탕으로 pd.DataFrame 형태로 만들어진 객체임. df 임.
print(df['이름']) # 이름에 대한 data들을 dataframe형태로 출력
print(df[['이름', '키']])  # 대괄호를 한번 더 감싸, 두가지 컬럼에 대한 data들을 dataframe 형태로 출력




# 2. Data Frame 객체 생성 ( Index 지정 ) ## Index 도 list 형태로 넣어줘야하네

df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
print(df)




# 3. Data Frame 객체 생성 ( Column 지정 ) ## data 중에서 원하는 column만 선택하거나, 순서 변경 가능
df = pd.DataFrame(data, columns= ['SW특기', '이름', '학교', '과학'])
print(df)
