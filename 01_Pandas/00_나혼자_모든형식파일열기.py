import pandas as pd

def read_csv(file_csv):
    encoding = ['utf-8', 'utf-8-sig', 'cp949', 'euc-kr']
    for enc in encoding:
        try:
            df = pd.read_csv(file_csv, encoding=enc)
        except UnicodeDecodeError:
            continue
        else:
            print('success to read your csv file')
            return df
        
def csv_to_excel(file_csv, file_xlsx):
    try:
        df = read_csv(file_csv)
    except Exception as e:
        print(f'fail to csv_to_excel : {e}')
        pass
    else:
        df.to_excel(file_xlsx)
        print('success to csv_to_excel')



# -------------------함수------------------------#
# def read_csv(file_csv) : csv file encoding 상관없이 읽기
# def csv_to_excel(file_csv, file_xlsx) : csv file을 excel file로 전환하기 

file_name = 'hello.csv' # csv file 명
file_xlsx = 'wow.xlsx' # xlsx file 명

csv_to_excel(file_name, file_xlsx)

