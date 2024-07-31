# mtcars 데이터셋(mtcars.csv)의 qsec 컬럼을 최소 최대 척도(Min-Max Scale)로
# 변환한 후 0.5보다 큰 값을 가지는 레코드 수를 구하시오.

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
df = pd.read_csv("SADF")
tmp = MinMaxScaler().fit_transform(df[['qesc']])
answer = (tmp>0.5).sum()
print(answer)

def min_max_scaler(x):
    answer = (x + x.min())/(x.max() - x.min())
    return answer
result = min_max_scaler(df['qsec']) #dataFrame
answer = len(result[result>0.5])
print(answer)
answer = (result>0.5).sum()
print(answer)



'''
# Standard Scaler 함수 생성
def standard_scaler(a):
    return (a - a.mean()) / a.std(ddof=0)

temp = standard_scaler(df['qsec'])
print(temp.mean(), temp.std(ddof=0))
# StandardScaler 객체 사용
from sklearn.preprocessing import StandardScaler # 평균을 0 표준 편차를 1로 만드는 친구!

temp = StandardScaler().fit_transform(df[['qsec']])

print(temp.mean(), temp.std(ddof=0))  # 표준정규분포 (평균 0, 표준편차 1)
'''

# 보스턴 데이터 범죄율 컬럼('CRIM')의 top10 중 10번째 범죄율 값으로 1~10위의 범죄율 값을 변경 후, 'AGE' 변수의 값이 80이상인 것에 대한 범죄율 평균을 산출하라.

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/boston.csv')
df.head(10)
tmp = df['CRIM'].sort_values(ascending = False).head(10)
df.loc[tmp.index,'CRIM']


# tmp = df['CRIM'].sort_values(ansending = False).head(10) # 10개 뽑기  # CRIM의 값을 기준으로 sort시킨다.
# df.loc[tmp.index,'CRIM'] = tmp.iloc[-1]
# result = df.loc[df.AGE>=80,'CRIM'].mean()

'''
## top 값을 구한다? DataFrame의 sort_values를 사용해서 정렬한다
# tmp = df.sort_values('CRIM',)
# print(dir(df.sort_values))
# print(help(df.sort_values))
tmp_df = df.sort_values('CRIM',ascending=False).head(10)
print(tmp_df)
'''
# 2-1-1) # Series.sort_values 사용
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/boston.csv')

# 1) 보스턴 데이터 범죄율 컬럼('CRIM')의 top10 구하기
A = df['CRIM'].sort_values(ascending=False).head(10)
# 2) 10번째 범죄율 값으로 1~10위의 범죄율 값을 변경하기
print(A.index)
df.loc[A.index, 'CRIM'] = A.iloc[-1]
# 3) (전체 데이터에서)'AGE' 변수의 값이 80이상인 것에 대한 범죄율 평균 구하기
result = df.loc[df.AGE >= 80, 'CRIM'].mean()
print(result)

# 2-1-1) # DataFrame.sort_values 사용
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/boston.csv')

# 보스턴 데이터 범죄율 컬럼('CRIM')의 top10 중 10번째 범죄율 값으로 1~10위의 범죄율 값을 변경 후, 'AGE' 변수의 값이 80이상인 것에 대한 범죄율 평균을 산출하라.
tmp_df = df.sort_values(by='CRIM', ascending=False).head(10)
df.loc[tmp_df.index, 'CRIM'] = tmp_df.iloc[-1,0] # 10번째 범죄율 값으로 1~10까지 모든 데이터를 변경
result = df.loc[df.AGE >= 80,'CRIM'].mean()

print(result)
print(result)

# print(help(df.sort_values))

# print(help(df))
A = df.sort_values("CRIM",ascending=False).head(10)
df.loc[A.index,'CRIM'] = A.iloc[-1,0]
result = df.loc[df.AGE >= 80,'CRIM'].mean()
print(result)
# loc [A,B] A : 조건이 들어간다. B는 어떤 feature 값을 가져올 건지 정한다.




A = df.sort_values('CRIM', ascending=False).head(10)
# A.index -> CRIM top10
# 10번째 범죄율 값으로 1~10위의 범죄율 값을 변경 후
# print(A.iloc[-1, 0]) # 10번 째 데이터를 가져온다.
df.loc[A.index, 'CRIM'] = A.iloc[-1, 0] # 모든 값을 A.iloc의 값으로 변경한다.
# 'AGE' 변수의 값이 80이상인 것에 대한 범죄율 평균을 산출하라.
result = df.loc[df.AGE >= 80, 'CRIM'].mean()
print(result)

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/boston.csv')
#print(df.head(10))
df2 = df['CRIM'].sort_values(ascending=False)
ten = df2.iloc[-1]
print(ten)
df.loc[df2.index, 'CRIM'] = ten
#print(df.loc[df2.index, 'CRIM'])
me = (df['AGE'] >= 80).mean()
print(round(me,2))

# 1-2. 하우징 데이터
# 'https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing.csv' 파일을 사용한다
# 주어진 데이터의 첫번째 행 부터 순서대로 80% 까지의 데이터를 추출 후
# 'total_bedrooms' 변수의 결측값(NA)을 'total_bedrooms' 변수의 중앙값으로 대체하고,
# 대체 전의 'total_bedrooms' 변수 표준편차값과 대체 후의 'total_bedrooms' 변수 표준편차 값을 산출하여
# 대체 전 표준편차 값 - 대체 후 표준편차 값을 구해 출력한다.


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing.csv')
print(df.shape)
print(df.head(2))
# 2-1-2) 계산 사용
df = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing.csv')

# 1) 첫번째 행 부터 순서대로 80% 까지의 데이터를 추출 df.shape[0]*0.8
# df.shape에서 [0]은 행의 수를
# df.shape[1] 은 열의 수를 반환한다.
print(df.shape[0])
p = int(df.shape[0]*0.8)
p = round(df.shape[0]*0.8)
print(p)

A = df.iloc[:p] # 80퍼까지 추출한 데이터를 A에 저장한다.

A_before = A['total_bedrooms']
print(A_before.head(20))
A_after = A_before.fillna(A['total_bedrooms'].median())
print(A_after.head(20))
# 2) 'total_bedrooms' 변수의 결측값(NA)을 'total_bedrooms' 변수의 중앙값으로 대체
A_before = A['total_bedrooms']
A_after = A_before.fillna(A['total_bedrooms'].median())



# 3) 대체 전 표준편차 값 - 대체 후 표준편차 값을 구해 출력
result1 = A_before.std(ddof=0) - A_after.std(ddof=0)
print(result1)


result1 = A_before.std(ddof=0) - A_after.std(ddof=0)
result2 = A_before.std(ddof=1) - A_after.std(ddof=1)
print(result1, result2)
print(round(result1, 3), round(result2, 3))
print(round(result1), round(result2)) # 반올림해서 정수로 변환

# 2-1-2)
# sklearn - train_test_split
from sklearn.model_selection import train_test_split
df = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing.csv')

A, test_df = train_test_split(df, train_size=0.8, shuffle=False)
A_before = A['total_bedrooms']
A_after = A_before.fillna(A_before.median())
print(test_df.shape)
print(A.shape)
print(df.shape)

result = A_before.std(ddof=0) - A_after.std(ddof=0)
print(round(result, 3))


# 'https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing.csv' 파일을 사용한다
# 하우징 데이터에서 'latitude' 컬럼의 이상치를 찾아 이상치들의 합을 산출하시오.
# 이상치 기준 : 평균 - (표준편차 * 1.5), 평균 + (표준편차 * 1.5)

# 평균 - (표준편차 * 1.5), 평균 + (표준편차 * 1.5)
# 이상치 기준 : 평균 - (표준편차 * 1.5), 평균 + (표준편차 * 1.5)
# 2-1-3)
import pandas as pd   # sample -> ddof=1
df = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing.csv')
A = df['latitude']


mean, std = A.mean(), A.std(ddof=1)
min_value = (mean) - std*1.5
max_value = (mean) + std*1.5
total_answer = A[A<min_value].sum() + A[A>max_value].sum()

print(total_answer)


mean, std = A.mean(), A.std(ddof=1)  # .std(ddof=1)
lower = mean - (std * 1.5)
upper = mean + (std * 1.5)
result = A[A < lower].sum() + A[A > upper].sum()
count_result = A[A < lower].shape[0] + A[A > upper].shape[0]

print(count_result)
print(result)
# 이상치에 해당하는 데이터 개수
df = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing.csv')

A = df['latitude']
mean, std = A.mean(), A.std(ddof=0)
lower = mean - (std * 1.5)
upper = mean + (std * 1.5)
result = A[A < lower].shape[0] + A[A > upper].shape[0]
print(result)
cond = (A < lower) | (A > upper)
result = A[cond].shape[0]
print(result)
# 이상치에 해당하는 데이터 검색
cond = (A < lower) | (A > upper)
df[cond]
#
# 결측치를 포함하는 모든 행을 제거한 후, 처음부터 순서대로 70%를 추출하여, 'housing_median_age' 컬럼의 사분위수 Q1의 값을 구하시오
#
# 주의사항 정답 제출시, 정수형으로 제출해야 함
# "https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing03.csv" 파일 사용
# # 한 문자형 컬럼에 빈칸 ''인 데이터 1건이 있어서
# # 빈칸을 결측으로 처리시 빈칸 제거전 242건에서 빈칸 제거후 243건의 행이 제거됨
# # 하지만 제거하지 않고 1분위수를 구하더라도 정답은 같음
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing03.csv")
df.head(2)

# 3-1-1)
from sklearn.model_selection import train_test_split
# print(help())
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing03.csv")
result_temp = df.isna().sum()

df = df.dropna()
# print(df)
A, _ = train_test_split(df,train_size=0.7,shuffle = False )

result = A['housing_median_age'].quantile(0.25)
print(result.astype('int'))
print(int(result))





# from sklearn.model_selection import train_test_split
# import pandas as pd

# df = pd.read_csv("https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/housing03.csv")

# # 결측치 확인
# #print(df.isna().sum())  # total_bedrooms        207


# # 1) 결측치를 포함한 모든 행 제거
# df = df.dropna(how='any', axis=0) # how='any, axis=0이 기본값

# # 2) 처음부터 순서대로 70%를 추출
# A, _ = train_test_split(df, train_size=0.7, shuffle=False)
# # A = df.iloc[:int(len(df)*0.7)]  # 다른 방법

# # 3) 'housing_median_age' 컬럼의 사분위수 Q1의 값 구하기
# result = A['housing_median_age'].quantile(0.25)

# # 4) 정수로 출력하기
# print(int(result))  # 정답 : 19
