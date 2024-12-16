# 상관계수 특징
# r은 -1과 1 사이에 존재
# r의 절댓값은 직선관계에 가까운 정도를 나타냄.
# 이떄 부호는 직선관계의 방향을 나타냄.
#
# 파이썬의 Standarddization 은 평균을 0 분산을 1로 만들어 준다.
# fit_transform은 train dataset에서만 사용이된다.
#
# transform은 train data로부터 학습된 mean값과 var 값을 testdata에 적용하기 위해 transform()을
# 사용한다.
#
# 왜 test_data는 fit_transform을 사용하지 않는가?
#
# train_test_split stratify
#
#
#
# 2,3 은 분류에서만 나왔는데, 회귀도 충분히 나올 수 있다.
#
# target(Y)
# 분류 분석 : 범주형, 혈액형, 성별 등을 맞춰라, 이미지를 보고 어떤 숫자인지 맞추어라,
#
# 회귀 분석 : 연속형, 판매량의 데이터(연속적인 데이터라면? 충분히 회귀분석이다. )
# 	주어진 값보다 더 큰 값, 작은 값, 사잇값 등이 있을 수 있는 것
# 회귀 분석의 종류
# Simple Linear Regression  x가 하나
# Multiple Linear Regression  x가 여럿
# Polynomial Regression 다항 회귀
# 	- 비선형 데이터 집합을 모델링할 때 사용
# 	- 곡선의 다항식 선을 사용함
# 	- 과대 적합이 나타나기 쉽다.
# 	- y 는 x의 n제곱들이 존재
# 	- x를 다항식으로 변경하여 모델링의 데이터로 사용
# Ridge, Lasso Regression
# 	- 독립변수들 간에 높은 상관 관계가  있는 경우 규제화를 통해 모델의 복잡도를 줄이는 방법
# 	- Ridgfe : 계수값을 0에 가깝게 만들지만 0이 되지 않음
# 	- Lasso : 계수 값을 0으로 만들 수 있음.
# 	- 얘네를 정규화 혹은 규제화라고 부른다.
#
#
#
#
#
#
