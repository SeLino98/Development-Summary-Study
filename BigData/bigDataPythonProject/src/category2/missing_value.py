
# 판다스 라이브러리 설치하기
# pip install pandas

import pandas as pd

# 데이터 타입을 변경시켜 보자.
# astype으로 일단 변형 시켜보고 에러가 나면 왜 안되는지 확인하자 .
# 오류 메세지에 따라 불필요한 문자를 제거하자.
data = {'point': ['1', '*2', '3', '*4', '1'],
        'date': ['2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06'],
        'gender': ['F', 'M', 'M', 'F', 'M']}
df = pd.DataFrame(data)
df.info()

# 불필요 문자 제거  (Series.replace(regex=True) 또는 Series.str.replace() 사용)
# df['point'].replace('\*','',regex=True).astype('int64')
# df['point'].astype('int64')
# df['point'].replace('\*','',regex=True).astype('int64')
df['new_point'] = df['point'].str.replace('*','').astype('int64')
df['new_date'] = df['date'].astype('datetime64[ns]')

df['new_dateTime'] = pd.to_datetime(df['date'],format='%Y-%m-%d')
df.info()
print(df['new_date'].dt.day.var()) #var가 0이 아니면 사용할 수 있다
print(df['new_date'].dt.day.nunique()) #
print(df['new_date'].dt.year.var()) #var가 0인 경우
print(df['new_date'].dt.year.nunique()) # nunique 가 1인 경우

#딕셔너리형태로 값 받기
df['day'] = df['new_date'].dt.day
df['gender_LE'] = df['gender'].replace({'F':0,'M':1})
df1 = df[['new_point','day','gender_LE']]
print(df1)






