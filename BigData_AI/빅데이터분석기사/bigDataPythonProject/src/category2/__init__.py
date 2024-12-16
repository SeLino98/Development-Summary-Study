#
# # 머신러닝의 이해
# ### 1-01. Supervised vs Unsupervised Learning
# - 지도학습(Supervised)
#    - 입력, 출력 데이터가 제공되는 학습
#    - 이미 알려진 사례를 바탕으로 일반화된 모델 구축
#    - 종류 : Regression, Classification
#    - 회귀(Regression) : 숫자화 된 데이터로 예측하는 것 (학습에서 주어진 것 이외의 작은 값, 사잇값, 큰 값이 있을 수 있음)
#    - 분류(Classification) : 어떤 데이터에 대한 category를 예측하는 것 (학습에서 주어진 것 이외에 다른 category 없음)
#
# - 비지도학습(Unsupervised)
#    - 입력은 주어지지만 출력은 제공되지 않음
#    - 기계가 알아서 학습하여 결과를 찾아내는 방법
#    - 종류 : Clustering, Demension Reduction, Association(연관)
#    - 군집화(Clustering) – 비슷한  특징을 가진 아이템을 그룹화 하는 것
#
# 머신러닝
# - 입력, 출력 : 숫자 데이터 사용 카테고리도 숫자로 바꿔서 사용한다는 뜻
# - 출력데이터가 숫자화 된 데이터 예측 (회귀) 범주 예측 (분류)
# - 키, 몸무게, 온도, 바람세기, 판매수량 : 회귀
# - 손글씨(0 ~ 9), 혈액형(A, B, AB, O : 0,1,2,3), 지역 : 분류
# # 이미 알려진 사례를 바탕으로 일반화된 모델 구축
# ### 1-02. 데이터 세트(Data Set)
# - Data Set : 머신러닝에서 입력(X), 출력(Y)에 사용되는 데이터 묶음
# - Data Set는 1개 이상의 입력과 1개의 출력으로 구성됨
# - 지도 학습에서 입력으로 사용되는 것이 X, 출력으로 사용되는 것이 Y
#   - X : **2차원 구조**이며, 1개 sample은 1차원 구조 임
#   - Y : **1차원 구조**, 1개 sample에 대한 target은 1개 scalar 값
# ### 1-03. 홀드 아웃(Hold out)
# - 성능 검증을 위해 Data Set을 Train Set, Test Set으로 분리하여 사용함
#   - Train Set은 학습에, Test Set은 성능 검증을 위해 사용됨
#   - 일반적으로 7:3 ~ 8:2로 많이 구분함
#
# - 본 수업에서의 데이터 이름
#   - X_train.csv : x_train, x_test
#   - Y_train.csv : y_train, y_test
#   - X_test.csv  : x_submission
#
# ### 1-04. 교차검증(Cross Validation)
#   - 데이터가 충분하지 않을 경우 Hold-out으로 나누면 많은 양의 분산 발생
#   - 이에 대한 해결책으로 교차검증을 사용할 수 있음
#   - 클래스 불균형 데이터에는 적합하지 않음
#   - 주어진 데이터를 가지고 반복적으로 성과를 측정하여 그 결과를 평균한 것으로 모형 평가
#   - 이미지출처 : https://chrisjmccormick.wordpress.com/2013/07/31/k-fold-cross-validation-with-matlab-code/
#
#
#
#
# ### 2-02. 데이터 전처리
# - sklearn.preprocessing.StandardScaler
# StandardScaler는 표준편차 평균이 필요한데, fit 메서드가 이걸 도와준다.
#
#    - **fit(X_train) : 전처리에 필요한 값 준비, return scaler만 해줌**
#    - **transform(X_train) : 전처리 실행, return 변환된 값으로 리턴 **
#    - **fit_transform(X_train) : 전처리에 필요 값 준비 및 처리, return 변환된 값으로 리턴 **
