# sample로 사용할 DataSet을 생성하는 함수 작성
# X: 국어, 영어, 수학 점수
# Y: 합격여부 (X의 평균 60이상, 과락 40점 미만)
# 사용할 라이브러리 import
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# seedno : 랜덤 수 생성 규칙
# size : 랜덤 수 생성 행의 수
# step=0 (균형), step=다른수 (불균형)
np.random.seed() # 랜덤의 규칙을 지정할 수 있다.


def make_sammple(seedno,size,step=0):
  np.random.seed(1234) # 1234라는 시드값을 줬다.
  size = 20 #sample의 갯수
  A = np.random.randint(0,101,(size,3))
  # print(A)
  df = pd.DataFrame(A, columns=["국어","영어","수학"])
  df['합격여부'] = (df.mean(axis=1)>=60) & (df.min(axis=1)>=40)
  print(df['합격여부'].value_counts())
  # F, T가 불균형하면 불균형 데이터라고 한다. step을 통해 불균형인지 아닌지 확인한다.
  if step ==0 :
    F, T = df['합격여부'].value_counts()
    B = np.random.randint(60,101,(F-T,3))
    df2 = pd.DataFrame(B,columns=["국어","영어","수학"])
    df2['합격여부'] = True
    df = pd.concat([df,df2])
    df.shape
    df['합격여부'].value_counts()
    df.index = pd.RangeIndex(len(df))
  df.info()
  df['합격여부'] = df['합격여부'].replace({True:1, False:0})
  df.tail(10)

data = make_sample(1234,20) # 균형 데이터로 만들고 싶을 때
data['합격여부'].value_counts()

data = make_sample(1234,20,1) # 불균형 데이터로 만들고 싶을 때
data['합격여부'].value_counts()
