import pandas as pd
import numpy as np
from statsmodels.api import Logit
df = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/bigdata/main/gender_classification.csv')
print(df.columns)
train = df.iloc[:210,]
test = df.iloc[210:,]
model = Logit.from_formula('gender ~ age + diameter + height + weight',train).fit()
print(model.summary())

## 오즈비 계산 np.exp와 coef를 이용한다.
# weight를 설명변수로 했을 때 오즈비는 ?
answer_1 = np.exp(model.params['weight'])
print(answer_1)

## 잔차 이탈도 구하기
'''
잔차이탈도(Residual Deviance)는 통계학에서 회귀 분석의 적합도를 평가하는데 사용되는 척도로 주로 로지스틱 회귀(Logistic Regression) 및 포아송 회귀(Poisson Regression)와 같은 일반화 선형 모델(Generalized Linear Models, GLMs)에서 사용된다.

llf: "최종 모델"의 로그 가능도(Log-Likelihood)를 나타냅니다. 여기서 최종 모델은 실제로 데이터에 적합한 회귀 모델을 의미합니다.
잔차 이탈도(Residual Deviance) = - 2 * llf
AIC(Akaike Information criterion) = -2 * llf + 2 * k (k = 모델의 파라미터 수)
model.aic 있음
'''
# Residual Deviance
rd = -2* model.llf
# AIC
aic = model.aic
print(rd)
print(aic)

# Error Rate  :: TEST 데이터 셋활용
y_pred_probs = model.predict(test)
predictions = (y_pred_probs >= 0.5).astype('int')
answer_c = np.mean(predictions != test['gender']) # 종속 변수인 gender와 예측값이 같은지 확인한다.
# 이때 예측한 값들이 0.5보다 클 때 해당 1로 전환하는 작업을 한다.
# 후에 종속 변수인 gender와 비교하여 예측값과 실제로 같은지 확인하고 출력한다.
print(answer_c)





