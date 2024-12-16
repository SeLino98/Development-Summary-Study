## 선형회귀 분석 OLS(Ordinary Least Squares)
## 선형회귀 분석 OLS 사용
import pandas as pd
XY = pd.read_csv('train1.csv')
X_submission = pd.read_csv('test.csv')

# [1] 다중선형회귀분석
# OLS만 쓰면 절편을 못 구한다. 때문에 add_constant를 사용해서 절편값을 구한다.

from statsmodels.api import OLS, add_constant
X = XY[['아빠', '엄마']]
Y = XY['아들']  # 연속형 종속변수

# y = coef1*X['아빠'] + coef2*X['엄마'] + 절편

X = add_constant(X) # 절편이 필요한 경우
print(X.head(10))
model = OLS(Y, X).fit()
print(model.summary())
# R-squared, Adj. R-squared
print(model.rsquared, model.rsquared_adj)
print(model.params)

'''
   const   아빠   엄마
0    1.0  175  160
1    1.0  180  158
2    1.0  172  155
3    1.0  174  161
4    1.0  178  163
5    1.0  168  160
6    1.0  173  168
7    1.0  177  167
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                     아들   R-squared:                       0.942
Model:                            OLS   Adj. R-squared:                  0.919
Method:                 Least Squares   F-statistic:                     40.62
Date:                Sat, 15 Jun 2024   Prob (F-statistic):           0.000809
Time:                        06:36:21   Log-Likelihood:                -9.3425
No. Observations:                   8   AIC:                             24.68
Df Residuals:                       5   BIC:                             24.92
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -3.8354     20.704     -0.185      0.860     -57.057      49.386
아빠             0.7722      0.099      7.772      0.001       0.517       1.028
엄마             0.2987      0.086      3.483      0.018       0.078       0.519
==============================================================================
Omnibus:                        0.189   Durbin-Watson:                   1.438
Prob(Omnibus):                  0.910   Jarque-Bera (JB):                0.345
Skew:                           0.222   Prob(JB):                        0.842
Kurtosis:                       2.085   Cond. No.                     1.42e+04
==============================================================================
'''

# 아들 키에 대한 예측 값 구하기
# 예측값 구하기
model.predict([[1.0, 175, 160],
               [1.0, 180, 158]])


# 직접 const 절편을 추가할 때
from statsmodels.api import OLS, add_constant
X = XY['아빠','엄마']
X = add_constant(X) # 절편이 필요한 경우


# 만약 파일로 데이터가 주어졌을때,
# id컬럼을 const컬럼으로 수정하여 사용
X_submission['id'] = 1
model.predict(X_submission.values)

# 만약 파일로 데이터가 주어졌는데, const 컬럼이 없는 경우 insert 사용
# const 컬럼을 추가하여 사용
X2 = X_submission[['아빠', '엄마']]
X2.insert(0, 'const', 1) # 0번째 컬럼에 const를 추가하고 1의 값을 넣는다.
model.predict(X2.values)


## 선형회귀분석 2개의 방법

# 아이스티 주문 예측 encoding이 필요한 경우 OLS 사용
# 종속 변수 : order
# 독립 변수 : weekday, hightemp
import pandas as pd
from statsmodels.api import OLS, add_constant
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('https://raw.githubusercontent.com/jmnote/zdata/master/simple-regression/iced-tea-orders.csv')
#print(df)
# 범주형 독립 변수의 경우이면서 정수형 값이 아닐 때 인코딩을 해야한다.
# 1. cat.codes으로 인코딩하는 방법
df['weekday'] = df['weekday'].astype('category').cat.codes # Object 타입인 weekday를 각 범주를 정수형 코드로 변환한다. 인코딩해준다.
# 2. LabelEncoder()으로 인코딩하는 방법
encoder = LabelEncoder()
df['weekday'] = encoder.fit_transform(df['weekday'])
X = df[['weekday', 'high_temperature']]
Y = df['order']
X = add_constant(X)
model = OLS(Y, X).fit() # OLS 모델 생성
print(model.params)

# 아이스티주문 예측 - OLS.from_formula 사용
'''
OLS.from_formula 함수와 함께 C()를 사용하면 범주형 변수인 weekday를 자동으로 인코딩해줍니다. 
이 방식은 상수 항 추가와 더미 변수 생성도 자동으로 처리해주기 때문에 코드가 훨씬 간단하고 직관적입니다.
'''
# 종속변수 : 'order'
# 독립변수 : 'weekday', 'high_temperature'
# 알아서 const, dummy 변수 잡아줌(encoding 불필요)
import pandas as pd
from statsmodels.api import OLS
df = pd.read_csv('https://raw.githubusercontent.com/jmnote/zdata/master/simple-regression/iced-tea-orders.csv')
print(df.head(3))
model = OLS.from_formula('order ~ C(weekday) + high_temperature', df).fit() # 범주형의 경우 C()로 묶는다.
# print(model.params)
print(model.summary())

import pandas as pd
from statsmodels.api import OLS
df = pd.read_csv("asdf")
model = OLS.from_formula('order ~ C(weekday) + high_temperature', df).fit()
print(model.summary)




