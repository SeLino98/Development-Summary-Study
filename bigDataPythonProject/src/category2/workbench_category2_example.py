# [0] 사용 라이브러리 import
import pandas as pd

# 데이타가 많은경우 모두 출력 안되고 ... 으로 생략해서 출력됨.
# 시험환경에서는 아래와 같이 해야해서 수정했습니다 ^^*
pd.options.display.max_rows = 500     #출력할 max row를 지정
pd.options.display.max_columns = 20   #출력할 max columns를 지정
#출력 format 지정 - 소수점아래 4자리까지
pd.set_option('display.float_format', '{:.4f}'.format)


# [1] 학습 데이터 X_train.csv 가져오기
X = pd.read_csv('bigdata/X_train.csv', encoding='cp949') #시험에서는 영어로 되어있기 때문에 encoding 해줄 필요는 없다.
print(X.head(2))

# [2] 학습 데이터 y_train.csv 가져오기
Y = pd.read_csv('bigdata/y_train.csv')
print(Y.head(2))

# [3] 제출용 데이터 X_test.csv 가져오기
X_submission = pd.read_csv('bigdata/X_test.csv', encoding='cp949')
print(X_submission.head(2))\

    ### 데이터 전처리
## 반드시 해야할 것!! 결측치 없도록!! type 통일화
# object datatime timedelta는 적절하게 변경해서 사용하자!!
# 1. 결측치 없도록 한다
# 2. dtype : int, float 만 가능함!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#    object, datetime64, timedelta64 -> 적절하게 변경


# [4] X, X_submission에 동일한 전처리를 위해 두 데이터 결합하기
# dfX로 이름 붙이기
dfX = pd.concat([X,X_submission], axis = 0,ignore_index=True)# 위에서 아래방향
print(dfX.tail(2))

# [5] 각 컬럼의 dtype 및 행, 열 개수 확인
dfX.info()
# 환불금액 쪽에 no null이 절반 나간거 보면 결측치가 있다는 것을 알 수 있다.

## 그럼 결측치를 처리해보자. 우선 결측치를 처리하기 전에 해당 사항을 다시한번알고가자
# 결측치 - 너무 많은 결측치를 가진 경우
# 1. 해당 컬럼을 제거하고 사용

# 2. 다른 값으로 채우기 - 범주형 변수 (새로운 범주 생성), 연속형 변수 (평균, 중앙값)
#  범주형이다 -> 새로운 범주를 생성한다.

# 연속형 변수 -> 평균, 중앙값으로 채운다.



# [6] dfX의 컬럼별 결측치 확인하기
dfX.isna().sum() # 환불금액에서 결측치를 확인할 수 있다.

# [7] 결측치를 채우기 위한 값 선정을 위한 작업
# 주구매상품별로 환불금액 평균이 다름을 확인
# tmp = dfX.groupby('주구매상품')['환불금액'].mean()

tmp = dfX.groupby('주구매상품')['환불금액'].transform('mean')
print(dfX['주구매상품'].head(5))
print(tmp)

# [8] '주구매상품'별 '환불금액' 평균으로 '환불금액'의 결측치를 채우기 한다
# 채우기 한 뒤 '환불금액'으로 추가한다.

tmp = dfX.groupby('주구매상품')['환불금액'].transform('mean')
dfX['환불금액'].mask(dfX['환불금액'].isna(),tmp)

# [9] '환불금액' 컬럼의 결측치 행을 확인해 본다
dfX[dfX['환불금액'].isna()]

# [10] '주구매상품'별 평균을 구할 수 없는 경우 '환불금액'을 '환불금액'의 평균으로 채우기 합니다.
# 채우기 후에 채우기가 잘 적용되었는지 확인합니다.
dfX['환불금액'].fillna(dfX['환불금액'].fillna(dfX['환불금액'].mean()))






