# 라이브러리 불러오기
import pandas as pd

# gt.txt 
dir_path = input('gt.txt가 있는 폴더의 경로를 입력하세요')

# gt.txt 파일 전처리
file_path = dir_path + 'gt.txt' # gt.txt 파일경로
df = pd.read_csv(file_path, sep='\t', header=None) # 파일 읽어오기
df.columns = ['filename', 'words'] # 컬럼 이름지정
df['filename'] = df['filename'].str[7:] # 문자열 슬라이싱

# labels.csv 파일로 저장
file_path = dir_path + 'labels.csv' # 파일경로
df.to_csv(file_path, index=False, encoding='euc-kr') # 저장