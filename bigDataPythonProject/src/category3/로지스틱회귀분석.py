
# 로지스틱 회귀분석 모델링 -분류 모형
# # 주의사항 - 이항분류!만 가능하다. 즉 (Yes, No) (F, M) 식으로 된 것들에 대해서만 사용이 가능하다.

# 종속변수 : 'special_sales'  (범주형)
# 독립변수 : 'busy_day' (범주형),'high_temperature' (연속형)

import pandas as pd
from statsmodels.api import Logit, add_constant
df = pd.read_csv("")

X = df[['busy_day','high_temperature']]
Y = df['special_sales']
X = add_constant(X)
print(X.head(4))
model = Logit(Y,X).fit()
print(model.param)

"""
   const  busy_day  high_temperature
0    1.0         0                28
1    1.0         0                24
Optimization terminated successfully.
         Current function value: 0.423859
         Iterations 7
const              -15.203506
busy_day             2.442647
high_temperature     0.544505
dtype: float64
"""

#  예측값 구하기
result_proba = model.predict([[1.0, 0, 20],
                              [1.0, 1, 30],
                              [1.0, 1, 20]])  # -> predict_proba(Y=1)
result = result_proba.round()  # cut_off = 0.5
print(result_proba)
print(result)

# 오즈 비율 구하기
# 오즈 비율(Odds Ratio)은 통계학과 의학 연구에서 두 가지 사건의 발생 가능성을 비교하는 데 사용되는 측도
# 다른 설명변수들이 고정되어있을 때 high_temperature가 한단위 증가하면
# special_sales가 성공(1)일 오즈가 1.724배 증가한다.
import numpy as np
coef = model.params['high_temperature']
result = np.exp(coef) #high_temperature의 회귀 계수
print(round(result,4)) # 1.724

# Logit, from_formula 사용
# 로지스틱 회귀분석 모델링 - 분류 모형
# 종속변수 : 'special_sales'  (범주형)
# 독립변수 : 'busy_day' (범주형),'high_temperature' (연속형)
import pandas as pd
from statsmodels.api import Logit

filename = 'https://raw.githubusercontent.com/jmnote/zdata/master/logistic-regression/special-sales.csv'
df = pd.read_csv(filename)
model = Logit.from_formula('special_sales ~ C(busy_day) + high_temperature',df).fit()
print(model.params)
'''
Optimization terminated successfully.
         Current function value: 0.423859
         Iterations 7
Intercept          -15.203506
C(busy_day)[T.1]     2.442647
high_temperature     0.544505
dtype: float64
'''

## 데이터 예측
# from_formula를 사용했을 때  predict를 하려면 독립변수들을 컬럼명으로 하는 DataFraem을 작성해야 한다.
data = pd.DataFrame({'busy_day':[0,1,1,0], 'high_temperature':[20,30,20,30]})
result = model.predict(data)
print(result)
'''
0    0.013211
1    0.972730
2    0.133455
3    0.756145
dtype: float64
0    0
1    1
2    0
3    1
dtype: int64
'''


