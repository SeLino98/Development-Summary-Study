
# 판다스 라이브러리 설치하기
# pip install pandas

import pandas as pd


data_train = {'아빠' : [175, 180, 172, 174, 178, 168, 173, 177],
        '엄마' : [160, 158, 155, 161, 163, 160, 168, 167],
        '아들' : [178, 182, 175, 180, 183, 174, 179, 183],
        '딸' : [163, 168, 157, 164, 167, 158, 169, 169]}
df = pd.DataFrame(data_train)
df.index.name = 'id'
df[['아빠', '엄마']].to_csv('X_train.csv')
df[['아들']].to_csv('Y1_train.csv')
df[['딸']].to_csv('Y2_train.csv')

data_test = {'아빠' : [174, 179, 180],
             '엄마' : [160, 160, 160]}
df2 = pd.DataFrame(data_test)
df2.index.name = 'id'
df2.to_csv('X_test.csv')

# [0] train, test 파일 가져오기
X_train = pd.read_csv('X_train.csv')
Y1_train = pd.read_csv('Y1_train.csv')
X_test = pd.read_csv('X_test.csv')
print(X_test)

# [1] 아빠, 엄마, 아들 키의 상관관계
# X 와 Y를 합칮나. 상관관계(피어슨 상관계수)
df = X_train.copy()
df['아들'] = Y1_train['아들']
print(df.corr())

# [2] 데이터 지정하기
# 아빠, 엄마의 키를 사용해 아들의 키를 예측 (X=[아빠, 엄마], Y1=[아들])
X = df[['아빠','엄마']]
Y1 = df['아들']
print(Y1)

# [3] 아들 키를 예측하는 모델 만들어 분석하기
from sklearn.linear_model import LinearRegression # 회귀분석할 때 선형모델 중 LinearRegression 모델을 쓴다.

model = LinearRegression()
model.fit(X,Y1)

# [4] 아들 모델 성능 평가하기
model.score(X,Y1) # 원래 평가하는 데이터를 따로 줘야된다,

# [5] 결과를 표로 작성하기 (예측, 오차)
result = df[['아빠', '엄마','아들']]
result['아들예측'] = model.predict(X)
result['아들오차'] = result['아들'] - result['아들예측']
result

# [6] 새로운 데이터로 예측하기
아빠키 = int(input('아빠키를 입력해 주세요 : '))
엄마키 = int(input('엄마키를 입력해 주세요 : '))
data = [[아빠키, 엄마키]]
아들키 = model.predict(data)
print(f'아들의 예상키는 {아들키[0]}입니다')

# [7] 새로운 데이터로 확인하기 - X_test.csv 로 확인하기
print(X_test)
Xt = X_test[['아빠','엄마']]
print(Xt)
model.predict(Xt)





