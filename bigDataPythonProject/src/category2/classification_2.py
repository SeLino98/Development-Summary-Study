# 모델 학습 및 성능 평가 함수 생성
# 순서 반드시 암기

# 사용할 라이브러리 import
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def ModelTrain(model,data):
  # 1) X,Y 데이터 분리
  Y = data['합격여부']
  X = data.drop(columns=["합격여부"]) # data에서 '합격 여부 컬럼을 제외한 모든 컬럼을 X 로 사용한다. DROP!!

  # 2 ) 학습, 평가 데이터로 분리
  X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, stratify = Y, random_state = 0)


  # 3 ) 분리된 데이터의 shape 출력
  print([X.shape for x in [X_train, X_test, Y_train, Y_test]])
  print(X_train.shape,X_test.shape, Y_train.shape, Y_test.shape)

  # 4 ) 학습 모델 선택, 학습
  model = LogisticRegression(max_iter=1000)
  model.fit(X_train,Y_train)

  # 5 ) 성능평가 - 정확도(Accuracy)
  # train, test 성능을 모두 확인하여 과대적합 여부를 확인해야 한다.!!
  print('train 성능 : ', model.score(X_train,Y_train))
  print('test 성능 : ', model.score(X_test,Y_test))
  return model

def make_sample(seedno,size,step):
    np.random.seed(seedno)
    A = np.random.randint(0,101,(size, 3))
    df = pd.DataFrame(A,columns=["국어","영어","수학"])
    df['합격여부'] =(df.mean(axis=1)>60) & ((df.min(axis=1))>=40)

    #균형 데이터라면? step ==0일 때
    # true 데이터를 추가한다. (false 값이 기본적으로 많이 나오기 때문에 )
    if step == 0:
        F, T = df['합격여부'].value_counts()
        B = np.random.randint(60, 101, (F - T, 3))
        df2 = pd.DataFrame(B, columns=["국어", "영어", "수학"])
        df2['합격여부'] = True
        df = pd.concat([df, df2])
        df.shape
        df['합격여부'].value_counts()
        df.index = pd.RangeIndex(len(df))
    return df



## 데이터 양이 많고 데이터가 균형적일 때 모델의 성능이 더 뛰어나다는 것을 알 수 있다.
# 또한 데이터의 양이 부족할 땐 파생 변수를 활용하여 성능상승을 시도할 수 있고,
# 데이터 단위가 다른 경우 스케일링 작업을 통해 성능상승을 할 수 있다.
# 정리하면 성능을 올리기 위해, 데이터 양을 증가 시키고, 균형적인 데이터 값과, 필요하다면 파생변수나 스케일링 작업을 시도하자.
# 균형 데이터   # 1234, 1225, 1245
for no in [1234, 1225, 1245] :
    model1 = LogisticRegression(max_iter=1000)
    data = make_sample(seedno=no, size=20000,step = 0)
    ModelTrain(model1, data)

# 불균형 데이터
for no in [1234, 1225, 1245] :
    model2 = LogisticRegression(max_iter=1000)
    data = make_sample(seedno=no, size=32000, step=1)
    ModelTrain(model2, data)

# 부족한 데이터   # 1234, 1225, 1245
for no in [1234, 1225, 1245] :
    model3 = LogisticRegression(max_iter=1000)
    data = make_sample(seedno=no, size=40, step=0)
    ModelTrain(model3, data)

# 부족한, 불균형 데이터 # 1234, 1225, 1245
for no in [1234, 1225, 1245] :
    model4 = LogisticRegression(max_iter=1000)
    data = make_sample(no, 60, step=1)
    ModelTrain(model4, data)


## 파생변수 사용
# 파생 변수를 사용해서 성능을 개선하자. 하지만 잘못사용하면 성능이 오히려 저하될 수 있다.
data = make_sample(seedno=1245,size=2000,step=0)
print(data.head(2))
# 파생변수 생성/추가
data['평균'] = data[['국어', '영어', '수학']].mean(axis=1)
data['최저'] = data[['국어', '영어', '수학']].min(axis=1)

for no in [1234, 1225, 1245] :
    model5 = LogisticRegression(max_iter=1000)
    data = make_sample(seedno=no, size=20000)
    data['평균'] = data[['국어', '영어', '수학']].mean(axis=1)
    data['최저'] = data[['국어', '영어', '수학']].min(axis=1)
    ModelTrain(model5, data)

# 모든 값을 사용한 예측 결과
def make_all():
    colnames = ['국어', '영어', '수학']
    data = [[kor, eng, mat] for kor in range(101) for eng in range(101) for mat in range(101)]
    data = pd.DataFrame(data, columns=colnames)
    data['평균'] = data[['국어', '영어', '수학']].mean(axis=1)
    data['최저'] = data[['국어', '영어', '수학']].min(axis=1)
    data['합격여부'] = (data['평균'] >=60) & (data['최저'] >= 40)
    data['합격여부'] = data['합격여부'].replace({True:1, False:0})  # 합격:1, 불합격:0 (레이블 인코딩)
    return data

data = make_all()
X1 = data.iloc[:, :3]
X2 = data.drop(columns=['합격여부'])
Y = data['합격여부']
print(Y.value_counts())

for x in model1, model2, model3, model4:
    print(x.score(X1, Y))
print(model5.score(X2, Y))


## 스케일러를 사용해보자.
# StancardScaler 사용하여 정규 분포 만들기
from sklearn.preprocessing import StandardScaler

for no in [1234, 1225, 1245] :
    model6 = LogisticRegression(max_iter=1000)
    data = make_sample(seedno=no, size=20000,step=0)
    data['국어'] *= 500
    data['수학'] *= 1000
    ModelTrain(model6, data)


for no in [1234, 1225, 1245]:
    model7 = LogisticRegression(max_iter=1000)
    data = make_sample(seedno=no, size=20000,step=0)
    data['국어'] *= 500  #일부로 데이터 단위가 차이가 많이나게 설정해보자.
    data['수학'] *= 1000 #일부로 데이터 단위가 차이가 많이나게 설정해보자.
    X = data[['국어', '영어', '수학']]
    Y = data['합격여부']
    scaledX = StandardScaler().fit_transform(X) #단위 차이가 많이나는 경우 스케일링 작업을 통해 작업하자.
    scaledX = pd.DataFrame(scaledX, columns=['국어', '영어', '수학'])
    data = pd.concat([scaledX, Y], axis=1)
    ModelTrain(model7, data)




