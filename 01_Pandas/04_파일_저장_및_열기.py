# DataFrame 파일 저장 및 열기 : DataFrame 객체를 excel, txt, csv 등의 형태의 파일로 저장 및 열기

from cv2 import DFT_COMPLEX_INPUT
import pandas as pd

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

df = pd.DataFrame(data)
df.index.name = '지원번호'

# # 1. csv 파일로 저장 # df. 누르면 뒤에 to_csv, to_excel, to_pickle 등 df를 저장할 수 있는 여러 형태가 나옴.
df.to_csv('hello.csv', encoding='utf-8-sig') # 한글 깨지면 enconding 옵션 넣기
df.to_csv('hello.csv', encoding='utf-8-sig', index=False) # index를 빼고 싶어용


# # 2. txt 파일로 저장
df.to_csv('hello.txt', sep='\t') # tab으로 구분된 (sep) txt 파일 저장가능


# # 3. excel 파일로 저장
df.to_excel('hello.xlsx')


# 4. csv 파일 열기 ## pandas 메소드 중 읽는 것들. pd.read_ 까지 누르면 뒤에 csv, txt, excel 등 있음 
df = pd.read_csv('hello.csv')
df = pd.read_csv('hello.csv', skiprows=1) # 파일에서 DataFrame 가져올때 row를 건너뜀.
df = pd.read_csv('hello.csv', skiprows=[1,3,4])
df = pd.read_csv('hello.csv', nrows=4) # 지정된 갯수 만큼의 row만 가져옴
print(df)

# df.to_csv('가공된버전.csv', encoding='utf-8-sig')



# 5. txt 파일 열기
df = pd.read_csv('hello.txt', sep='\t', index_col='지원번호') # 읽을때 sep는 구분자로 가져옴. # index_col를 통해 column을 index로 지정해서 가져옴.
df.set_index('지원번호') # 이것도 위와 동일하게 index를 지원번호 column으로 가져오는 것임.
print(df)


# 6. excel 파일 열기
df = pd.read_excel('hello.xlsx', index_col='지원번호')
print(df)

