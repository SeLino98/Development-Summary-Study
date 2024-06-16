# 예측값 및 신뢰구간(CI라고 부르며 get_prediction으로 구한다. )
# OLS 모델
# mean : 예측값의 평균
# mean_se : 예측값의 표준 오차(Standard Error)
# mean_ci_lower: 예측값의 신뢰구간의 하한
# mean_ci_upper: 예측값의 신뢰구간의 상한
# obs_ci_lower: 개별 관측치에 대한 예측 신뢰구간의 하한(a confidence interval for a new observation)
# obs_ci_upper: 개별 관측치에 대한 예측 신뢰구간의 상한
# (ci: confidence intervals) : 신뢰 구간
# Logit 모델
#
# predicted : 예측값의 평균
# se : 예측값의 표준 오차(Standard Error)
# ci_lower: 예측값의 신뢰구간의 하한
# ci_upper: 예측값의 신뢰구간의 상한

import pandas as pd
from statsmodels.api import OLS, add_constant
df = pd.read_csv('https://raw.githubusercontent.com/jmnote/zdata/master/simple-regression/iced-tea-orders.csv')
print(df.head(2))
model = OLS.from_formula('order ~ C(weekday) + high_temperature',df).fit()

print(model.params)
"""
Intercept            -9.283019
C(weekday)[T.Mon]     4.622642
C(weekday)[T.Sat]    -0.155660
C(weekday)[T.Sun]     7.933962
C(weekday)[T.Thr]     1.500000
C(weekday)[T.Tue]    -0.622642
C(weekday)[T.Wed]    11.212264
high_temperature      2.688679
dtype: float64
"""
## get_prediction
# 예측에 사용할 데이터
data = pd.DataFrame({'weekday':['Sat'],'high_temperature':[30]})
result = model.get_prediction(data)

summary = result.summary_frame(alpha=0.05)
print(summary)# 95퍼의 신뢰구간 // 5퍼의 유의수준
data = pd.DataFrame({'weekday':['Sat'], 'high_temperature':[33]})
result = model.get_prediction(data)
print(result.summary_frame(alpha=0.05)) # 예측값 + 95% 신뢰구간 하한, 상한
print(result.predicted_mean) # 예측값
print(result.conf_int(alpha=0.05))  # 95% 신뢰구간 하한, 상한


















