# Index : Data에 접근할 수 있는 주소 값

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

import pandas as pd

# 1.  # DataFrame의 Index 지정해주기 
df = pd.DataFrame(data, index= ['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])

# 2. df의 index를 list로 볼 수 있음
print(df.index) # df의 index를 list로 볼 수 있음

# 3. df의 index의 name을 지정해 줄 수도 있음.
df.index.name = '지원번호'
print(df)

# 4. index 초기화
df.reset_index()
print(df)

# 5. 원래 쓰던 index '지원번호' 인덱스 삭제, inplace 필수
df.reset_index(drop=True, inplace=True)
print(df)

# 6. Index 설정 : 지정한 column으로 Index를 설정

df.set_index('이름', inplace=True) # index를 set팅 합니다 .이름이라는 column을
df.set_index('수학', inplace=True)
print(df)

# 7. Index 정렬 : Index를 기준으로 오름차순, 내림차순 정렬
df.sort_index(ascending=False) # index를 sort(정렬) 합니다. 순서를 내림차순으로.
print(df)

