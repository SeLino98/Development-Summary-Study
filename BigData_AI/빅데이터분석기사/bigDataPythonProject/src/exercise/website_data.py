import pandas as pd

#### $1
# 실제 시험에서는 데이터 csv 파일들이 미리 제공이 된다.
# 하지만 데이터에 대해서 이해를 해봐야 하니
# 데이터 생성을 해보자 .
# 데이타가 많은경우 모두 출력 안되고 ... 으로 생략해서 출력됨.
# 시험환경에서는 아래와 같이 해야해서 수정했습니다 ^^*
pd.options.display.max_rows = 500     #출력할 max row를 지정
pd.options.display.max_columns = 20   #출력할 max columns를 지정
#출력 format 지정 - 소수점아래 4자리까지
pd.set_option('display.float_format', '{:.4f}'.format)

## 데이터를 csv 파일로 읽고 해당 데이터의 모습을 가늠한다.
df = pd.read_csv('bigdata/daily-website-visitors.csv')
print(df.shape) # 데이터의 행과 열의 정보를 볼 수 있다.
print(df.head(2)) # 데이터의 실제 모습을 2개까지 확인해본다.

# 컬럼명에서 수정하고픈 컬럼명을 수정한다.
df.columns = df.columns.replce('.','_',regex = False).str.lower()
print(df.columns)
###
#   row : 1번 부터 시작하는 일련번호
# day : 요일 정보
# day_of_week : 요일 정보
# date : 날짜 정보
# page_loads : 로드된 일별 페이지 수
# unique_visits : 6시간 이상 페이지에서 조회되지 않은 IP 주소의 일일 방문자 수 (종속변수)
# first_time_visits : 이전 고객으로 식별되는 쿠키를 가지고 있지 않은 고유 방문자 수
# returning_visits : unique_visits 수에서 first_time_visits 제외
#   ###
print(df.dtypes)


## 데이터 정제 과정
# 여기서 unique_visites의 값을 예측하는 값으로 사용할 것이다. -> 이 값은 object 타입인데, 수치데이터로 변경해줘야 한다.
df['unique_visits'] = df['unique_visits'].replace(',','',regex=True).astype(int) # 인트형의 수치 데이터로 바꾼다.


# 시험 형식으로 train, test 데이터로 나누어 저장한다. (6:4)비율로 해보자
train_size = len(df) - int(len(df)*0.4) # 0.6이 된다 .
df = df.sample(frac=1,random_state=1234)
df['row'] = range(1,len(df)+1)
train = df.iloc[:train_size, :]
test = df.iloc[train_size:, :] # 데이터를 비율로 쪼갰다.
print(train, test)

y = 'unique_visits'
x_train = train.drop(columns=y) # unique_visits라는 속성 값을 날린다.
y_train = train[['row',y]]
x_test = test.drop(y) # unique_visits라는 속성 값을 날린다.
y_test = test[['row',y]]

## CSV 파일로 저장한다.
x_train.to_csv('x_train.csv',index=False)
y_train.to_csv('y_train.csv', index=False)
x_test.to_csv('x_test.csv', index=False)
y_test.to_csv('y_test.csv', index=False)



#### $2
# 데이터를 불러오고 전처리 과정을 담자 .
# 데이터 파일을 불러오자 .
x_training = pd.read_csv('x_train.csv')
x_submission = pd.read_csv('x_test.csv')
y_training = pd.read_csv('y_train.csv')
y_submission = pd.read_csv('y_test.csv')

# X의 training과 submission의 데이터를 묶어 전처리 하기 위한 dfX 를 만들자.
dfX = pd.concat([x_training, x_submission],ignore_index=True,axis=0) # 수직으로 합친다.
# dfX 의 정보를 확인해 보자.
print(dfX)
print(dfX.head(5))

# Object 타입으로 저장된 값들과 인스턴스 내에 값들의 값들 중 불순물들을 제거하자
dfX[['page_loads', 'first_time_visits', 'returning_visits']] \
    = dfX[['page_loads', 'first_time_visits', 'returning_visits']].replace(',', '', regex=True).astype(int)
# DataFrame 정보 출력
print(dfX.info())
'''
[ ]
# [4] 'page_loads', 'first_time_visits', 'returning_visits' 에 대해서
#  콤마를 없애고, int로 형변환 합니다
dfX['page_loads'].str.replace(',', '', regex=True).astype(int)
names = ['page_loads', 'first_time_visits', 'returning_visits']................................................................................................................................................................................................................................................
dfX[names] = dfX[names].replace(',', '', r
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2167 entries, 0 to 2166
Data columns (total 7 columns):
 #   Column             Non-Null Count  Dtype 
---  ------             --------------  ----- 
 0   row                2167 non-null   int64 
 1   day                2167 non-null   object
 2   day_of_week        2167 non-null   int64 
 3   date               2167 non-null   object
 4   page_loads         2167 non-null   int64 
 5   first_time_visits  2167 non-null   int64 
 6   returning_visits   2167 non-null   int64 
dtypes: int64(5), object(2)
'''
# date가 object 타입이다. 해당 타입을 형 변환시켜준다.
dfX['date'] = pd.to_datetime(dfX['date'],format='%m/%d/%Y')
# date에서 day day_of_week이 서로 같은 데이터이다.
dfX2 = dfX.drop(columns='day')
# date를 year, month, day 컬럼으로 나눈다. 제1정규화
# date 에서 year, month , day에 대한 정보를 dfX에 포함시키고
# date를 제거한다.
date = pd.DataFrame()
tmp = dfX2[date].dt # DatetimeProperties의 접근자로 날짜와 시간을 나타내는 열에서 연도, 월 일 등을 쉽게 추출할 수 있게 한다.
date['year'] = tmp.year
date['month'] = tmp.month
date['day'] = tmp.day
dfX3 = dfX2.drop(columns='date')
dfX3 = pd.concat([dfX3,date],axis=1) # dfX3에서 date 속성 값들을 추가시킨다.
print(dfX3.info())

# Y와 X의 feature의 관계를 분석해보기 위해 dfX3과 Y를 병합한다.
dfXY = pd.merge(dfX3,y_training)
print(dfXY.shape) # 잘 찍혔는지 확인한다.


# X Y의 상관계수를 확인한다.
# 이때 보면 unique_visit(종속변수)과 상관성이 매우 높은 feature들이 있다.
print(dfXY.corr()['unique_visits'])
'''
row                  0.0162
day_of_week         -0.2592 
page_loads           0.9885 V 
first_time_visits    0.9962 V
returning_visits     0.9059 V 얘네가 상관성이 가징 넢은 친구들이다 . 
year                 0.0707
month               -0.0478
day                 -0.0353
unique_visits        1.0000
Name: unique_visits, dtype: float64
'''
# day_of_week 별 유니큐 비짓과 관련된 걸 찾아본다
# [1] day_of_week
tmp = dfXY.groupby('day_of_week')['unique_visits'].mean()
high_day_of_week = tmp[tmp>3000].index.values # day_of_week 별 평균이 높은 것에 대한 데이터를 high_day_of_week로 저장한다.
# [2] month
tmp = dfXY.groupby('month')['unique_visits'].mean()
high_month = tmp[tmp>3000].index.values
# [1], [2]의 연관성을 확인해보니
# [1] 2, 3, 4, 5 가 높고 1, 6, 7이 낮은 것을 볼 수 있다.
# [2] 2, 3, 4, 5, 10, 11이 높고 1, 6, 7이 낮은 것을 볼 수 있다.
# [1] [2] 를 통해 파생변수를 생성한다.
import numpy as np
dfX3['dow_h'] = dfX3['day_of_week'].isin(high_day_of_week).astype(int)
dfX3['month_h'] = dfX3['month'].isin(high_month).astype(int)


#### $3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge, Lasso
## 다양한 모델을 만들고 성능을 출력해보자.
# 함수를 두 개 만들 것이다.
# 데이터 성능을 돌리는 함수
# 데이터 모델을 사용하는 함수
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_squared_log_error as msle
import numpy as np

# [1] 데이터 성능을 테스트 하느 모델
def get_scores2(model,xtrain, xtest,ytrain, ytest):
    '''
    r2_score: 결정계수 R^2
    mae: 평균 절대 오차.
    mse: 평균 제곱 오차.
    np.sqrt: 제곱근을 계산하여 RMSE를 구함.
    '''
    # 예측값
    pred1 = model.predict(xtrain)
    pred2 = model.predict(xtest)
    # MAE MSE RMSE 등은 모델이 예측한 값과 실제 값 간의 차이를 측정하여 모델의 정확성을 평가하는 데 도움을 준다.
    # 각 지표는 서로 다른 방식으로 오류를 계산하며, 특정 상황에서 더 적합하게 나타내게 할 수 있다.

    train_R2 = r2_score(ytrain,pred1) # train 데이터에 대한 R2 점수
    test_R2 = r2_score(ytest,pred2) # test 데이터에 대한 R2 점수
    MAE = mae(ytest, pred2) # test데이터에 대한 평균 절대 오차
    MSE = mse(ytest,pred2) # 평균 제곱 오차
    RMSE = np.sqrt(MSE) # 평균 제곱근 오차

    #msle와 rmsle 계산을 위한 음수 값 처리
    pred2 = np.where(pred2 < 0, 0 , pred2) # 예측값이 음수일 경우 0으로 변환
    MSLE = msle(ytest,pred2) # 평균 제곱 로그 오차
    RMSLE = np.sqrt(MSLE) # 평균 제곱근 로그 오차

    # 계산된 성능 지표를 소수점 4자리까지 반올림
    data = [round(x,4) for x in [train_R2,test_R2,MAE,MSE,MSLE,RMSLE]]
    names = 'r2_train trtest mae mse msle rmse rmsle'.split(' ')

    # 성능 지표를 pandas Series로 저장
    scores = pd.Series(data, index=names)
    return scores



# 다양한 모델에 대한 성능을 출력하는 함수 작성
# dataFrame으로 만든다.
def make_models(xtrain, xtest, ytrain, ytest, n=300, RL=False):
    temp = pd.DataFrame()

    model1 = LinearRegression().fit(xtrain, ytrain)
    temp['model1'] = get_scores2(model1, xtrain, xtest, ytrain, ytest)

    if not RL:
        model2 = DecisionTreeRegressor(random_state=0).fit(xtrain, ytrain)  # overfitting 나기 쉬움
        temp['model2'] = get_scores2(model2, xtrain, xtest, ytrain, ytest)

        for d in range(3, 9):
            model2 = DecisionTreeRegressor(max_depth=d, random_state=0).fit(xtrain, ytrain)
            temp[f'model2_{d}'] = get_scores2(model2, xtrain, xtest, ytrain, ytest)

        model3 = RandomForestRegressor(n, random_state=0).fit(xtrain, ytrain)
        temp['model3'] = get_scores2(model3, xtrain, xtest, ytrain, ytest)

        for d in range(3, 9):
            model3 = RandomForestRegressor(n, max_depth=d, random_state=0).fit(xtrain, ytrain)
            temp[f'model3_{d}'] = get_scores2(model3, xtrain, xtest, ytrain, ytest)

    model4 = XGBRegressor(objective='reg:squarederror').fit(xtrain, ytrain)
    temp['model4'] = get_scores2(model4, xtrain, xtest, ytrain, ytest)

    if RL:
        for a in [0.01, 0.1, 1, 2]:
            model5 = Ridge(alpha=a).fit(xtrain, ytrain)
            temp[f'model5_{a}'] = get_scores2(model5, xtrain, xtest, ytrain, ytest)

        for a in [0.01, 0.1, 1, 2]:
            model6 = Lasso(alpha=a).fit(xtrain, ytrain)
            temp[f'model6_{a}'] = get_scores2(model6, xtrain, xtest, ytrain, ytest)


    temp = temp.T
    temp.insert(2, 'diff', (temp['r2_train'] - temp['r2_test']).abs())

    return temp




















