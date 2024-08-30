import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import shap
import lightgbm as lgb

train = pd.read_csv(r"C:\Users\Administrator\Desktop\82407_KCB_financial_style_data\credit_card_data.csv")

# 예측에 필요없다고 판단되는 컬럼 값들을 버린다. 나이(avg_rat 등)에 경우 너무 상관계수가 높아서 뺌. 의미없는 데이터 또한 제거.
features = train.drop(
    columns=['avg_score', 'avg_rat', 'population', 'year', 'month', 'ages', 'city', 'pop_cd', 'sex', 'monthly_cd_loan',
             'monthly_insurance_loan'
             ])  # ,'monthly_bk_loan','monthly_loan','num_opencard','num_usecard'
# features = train.drop(columns=['avg_score', 'avg_rat', 'population', 'year', 'month', 'ages', 'city', 'pop_cd', 'sex', 'num_usecard'])
# 예측 모델 y 종속 변수
target = train['avg_score']

# train과 test 셋 분할
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# StandardScaler 작업을 통해 데이터 스케일링
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# LightGBM 모델 생성 및 학습
lgb_model = lgb.LGBMRegressor(n_estimators=5000, learning_rate=0.3)
lgb_model.fit(X_train, y_train)

# 예측 및 평가
predictions = lgb_model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f"LightGBM Model - MSE: {mse}, R^2: {r2}")

# # 시각화
# importance = lgb_model.feature_importances_
# feature_names = features.columns
# indices = np.argsort(importance)
# plt.figure(figsize=(10, 8))
# plt.title('Feature Importances - LightGBM')
# plt.barh(range(len(indices)), importance[indices], color='b', align='center')
# plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
# plt.xlabel('Relative Importance')
# plt.show()
#
# # SHAP values 계산
# explainer = shap.TreeExplainer(lgb_model)
# shap_values = explainer.shap_values(X_test)
#
# # SHAP 시각화
# shap.summary_plot(shap_values, X_test, feature_names=features.columns)  # SHAP 디폴트 시각 표
# shap.summary_plot(shap_values, X_test, feature_names=features.columns, plot_type="bar")  # 막대 플롯으로 확인

import pandas as pd

# 특정 컬럼만 산출해서 사용자 입력값을 받게 하고, 나머지 모델에 대해서는 평균 값으로 대치해서 사용하려고 했는데, 예측력이 떨어짐.
# 특정 컬럼만 산출해서 사용하려고 했던 이유는, 모든 컬럼을 다 사용할 경우 과적합 문제가 일어날 수 있기 때문,
# 그래서 진짜 의미가 없거나, 예측할 때 방해가 될 것 같은 컬럼 값을 제거.
#   ex 예측 모델에서 방해가 되는 feature
#   ex 대출 금액 등
# 1. 특정 컬럼만 산출해서 약 8개의 feature 했지만, 모델 성능이 좋지 않게 나옴,,, MSE R^2이 각각 구려졌음.!

# 2. 해당 산출 점수가 정말 의미가 있는 정보인지 궁금해서 방법을 생각해봤는데, 내 데이터를 입력해보고, 내 실제 신용 점수랑 매칭시켜보는 방법도 괜찮을까? -> 대출 정보나 신용 정보가 부족해서 정확하게 나오지 않을 것 같다.

# 3. 처음 CSV로 데이터를 볼 떄 이 데이터가 대체 어떤 feature값을 의미하는지 정확하게 아는 방법?. 보통 유추나 번역기를 통해 추론했습니다.

# 4. 모델마다 유효한 feature 값들이 다른데 이럴 경우에는 모델 시각화에서 가장 평탄한 값이 나온 것을 기준으로 삼아야 하는 건가?

# 5. 다른 시각 모델을 통해서 나온 값들에 대해 어떤 판단 지표를 가지고 내가 거르고 추가해야하는지?


# feature 목록 및 해당하는 한국어 번역
features = [
    'num_opencard', 'num_usecard',                # 보유 카드 수, 사용 카드 수
    'monthly_card_spend',                         # 월별 카드 사용액
    'monthly_lc',                                 # 월별 LC
    'monthly_loan',                               # 월별 대출금
    'monthly_bk_loan',                            # 월별 BK 대출
    'monthly_installments_loan',                  # 월별 할부 대출액
    'monthly_sbk_loan',                           # 월별 SBK 대출
    'loan_commitment',                            # 대출 약정
    'inst_rep_loanb',                             # 할부 상환 대출
    'ls_rep_loanb',                               # LS 상환 대출
    'credit_loan',                                # 신용대출금
    'mortgage_loan',                              # 주택 담보 대출
    'credit_card_payment',                        # 신용카드 결제액
    'credit_card_installments_payment'            # 신용카드 할부금액
]

# new_input = {
#     'num_opencard': 2,                           # 보유 카드 수
#     'num_usecard': 1   ,                          # 사용 카드 수
#     'monthly_card_spend': 450000,                # 월별 카드 사용액
#     'monthly_lc': 250000,  # 월별 LC
#     'monthly_loan': 600000,                      # 월별 대출금
#     'monthly_bk_loan': 200000,                   # 월별 BK 대출
#     'monthly_installments_loan': 1200000,        # 월별 할부 대출액
#     'monthly_sbk_loan': 300000,                  # 월별 SBK 대출
#     'loan_commitment': 800000,                   # 대출 약정
#     'inst_rep_loanb': 200000,                    # 할부 상환 대출
#     'ls_rep_loanb': 100000,                      # LS 상환 대출
#     'credit_loan': 5000000,                      # 신용대출금
#     'mortgage_loan': 3500000,                    # 주택 담보 대출
#     'credit_card_payment': 700000,               # 신용카드 결제액
#     'credit_card_installments_payment': 150000,  # 신용카드 할부금액
# }
# feature의 한국어 번역 매핑
feature_translation = {
    'credit_card_installments_payment': '신용카드 할부금액 (월별 신용카드 할부 결제 총액, 예: 10만원)',
    'credit_loan': '신용대출금액 (현재 대출 받은 금액, 예: 500만원)',
    'monthly_sbk_loan': '월별 SBK 대출 (저축은행에서 대출 받은 월별 금액, 예: 30만원)',
    'inst_rep_loanb': '할부 상환 대출 금액 (매월 할부로 상환 중인 대출 금액, 예: 20만원)',
    'credit_card_payment': '월별 신용카드 총 결제액 (신용카드로 매달 지출한 총액, 예: 70만원)',
    'monthly_card_spend': '월별 카드 사용액 (모든 카드에서 매달 지출한 총액, 예: 45만원)',
    'monthly_installments_loan': '월별 할부 대출액 (매월 할부로 상환 중인 대출의 총액, 예: 120만원)',
    'ls_rep_loanb': '일시불 대출 상환 금액 (일시불로 상환한 대출 금액, 예: 10만원)',
    'loan_commitment': '대출 약정 (현재 약정된 대출 금액, 예: 80만원)',
    'monthly_lc': '월별 대출 약정 (대출을 받기로 약정한 금액, 예: 25만원)',
    'mortgage_loan': '주택 담보 대출 (주택 담보로 받은 대출 금액, 예: 350만원)',
    'monthly_bk_loan': '월별 BK 대출 (BK 은행에서 받은 월별 대출 금액, 예: 20만원)',
    'monthly_loan': '월별 대출금액 (매달 상환 중인 대출 금액, 예: 60만원)',
    'num_opencard': '보유 카드 수 (보유하고 있는 카드의 총 수, 예: 2개)',
    'num_usecard': '사용 카드 수 (현재 사용 중인 카드의 총 수, 예: 1개)'
}

# feature_translation = {
#     'credit_card_installments_payment': '신용카드 할부금액 (ex : 월 내시는 할부 금액 )',
#     'credit_loan': '신용대출금액 ( 현재 대출 받은 금액 단위 WON ) ',
#     'monthly_sbk_loan': '월별 SBK 대출 (월 저축 은행 대출 금액 단위 WON )',
#     'inst_rep_loanb': '월 할부 상환 대출 금액 ( WON )',
#     'credit_card_payment': '월별 신용카드 총 결제액 ( WON )',
#     'monthly_card_spend': '월별 8금융 카드 사용액 ( WON )',
#     'monthly_installments_loan': '월별 할부 대출액 ( WON )',
#     'ls_rep_loanb': '일시불 대출 상환 금액 ( WON )',
#     'loan_commitment': '대출 채무 ( WON )',
#     'monthly_lc': '월별 대출 약정(대출 받기로 한 금액 없다면, 대출 받은 실제금액으로 작성 WON)',
#     'mortgage_loan': '주택 담보 대출 ( WON )',
#     'monthly_bk_loan': '월별 BK 대출 ( WON )',
#     'monthly_loan': '월별 대출금액 ( 이미 대출 받은 실제금액 WON) ',
#     'num_opencard': '8금융 은행의 보유 카드 수(개)',
#     'num_usecard': '8금융 은행의 실제 사용 카드 수(개)'
# }


def get_user_input(features, feature_translation):
    input_data = {}  #사용자가 입력한 데이터를 딕셔너리 형태로 반환.
    print("안녕하세요 제 8금융입니다. \n 고객님의 신용 점수를 예측해드리겠습니다. \n 신용 점수 예측을 위한 데이터를 입력해주세요 \n 모든 데이터는 수치로 입력해주세요 ex 10만원 -> 100000 ")
    for feature in features:
        while True:
            try:
                # feature의 한국어 번역 사용하여 사용자 입력 요청
                translated_feature = feature_translation.get(feature, feature)
                value = float(input(f"{translated_feature} 값을 입력하세요: "))
                input_data[feature] = value
                break
            except ValueError:
                print(f"{translated_feature} 값을 올바른 숫자로 입력하세요.")
    return input_data


def predict_credit_score(input_data, model, scaler, feature_columns):
    """
    사용자 입력 데이터를 기반으로 신용 점수를 예측하는 함수.
    """
    # 입력 데이터를 DataFrame 형태로 변환
    input_df = pd.DataFrame([input_data])

    # 입력 데이터가 모델의 피처와 동일한 순서를 가지도록 정렬
    input_df = input_df[feature_columns]

    # 스케일링
    input_scaled = scaler.transform(input_df)

    # 예측
    predicted_score = model.predict(input_scaled)

    return predicted_score[0]



# 사용자가 직접 입력
new_input = get_user_input(features, feature_translation)


# 예측 점수 계산
predicted_score = predict_credit_score(new_input, lgb_model, scaler, features)
print(f"예측된 신용 점수: {predicted_score:.2f}")


























































############################################################################################
#
# # 사용자로부터 입력받을 feature 목록
# features = [
#     'credit_card_installments_payment', 'credit_loan', 'monthly_sbk_loan',
#     'inst_rep_loanb', 'credit_card_payment', 'monthly_card_spend',
#     'monthly_installments_loan', 'ls_rep_loanb', 'loan_commitment',
#     'monthly_lc', 'mortgage_loan','monthly_bk_loan','monthly_loan','num_opencard','num_usecard'
# ]
#
#
# def get_user_input(features):
#     """
#     사용자가 입력할 수 있는 기능을 제공하여 데이터를 수집하는 함수.
#
#     Parameters:
#     - features (list): 사용자로부터 입력받을 feature들의 리스트.
#
#     Returns:
#     - input_data (dict): 사용자가 입력한 데이터를 딕셔너리 형태로 반환.
#     """
#     input_data = {}
#
#     print("신용 점수 예측을 위한 데이터를 입력하세요:")
#     for feature in features:
#         while True:
#             try:
#                 value = float(input(f"{feature} 값을 입력하세요: "))
#                 input_data[feature] = value
#                 break
#             except ValueError:
#                 print(f"{feature} 값을 올바른 숫자로 입력하세요.")
#
#     return input_data
#
#
# def predict_credit_score(input_data, model, scaler, feature_columns):
#     """
#     사용자 입력 데이터를 기반으로 신용 점수를 예측하는 함수.
#
#     Parameters:
#     - input_data (dict): 사용자가 입력한 데이터.
#     - model (LightGBMRegressor): 학습된 LightGBM 모델.
#     - scaler (StandardScaler): 학습에 사용된 스케일러.
#     - feature_columns (list): 모델에 사용된 피처들의 리스트.
#
#     Returns:
#     - predicted_score (float): 예측된 신용 점수.
#     """
#
#     # 입력 데이터를 DataFrame 형태로 변환
#     input_df = pd.DataFrame([input_data])
#
#     # 입력 데이터가 모델의 피처와 동일한 순서를 가지도록 정렬
#     input_df = input_df[feature_columns]
#
#     # 스케일링
#     input_scaled = scaler.transform(input_df)
#
#     # 예측
#     predicted_score = model.predict(input_scaled)
#
#     return predicted_score[0]
#
#
# # # 모델과 스케일러 로드 (이미 학습된 모델을 사용한다고 가정)
# # try:
# #     # LightGBM 모델을 임의로 로드 (모델이 저장된 위치에 따라 다름)
# #     lgb_model = lgb.LGBMRegressor(n_estimators=5000, learning_rate=0.3)  # 기본 모델 설정
# #     lgb_model.fit(...)  # 실제 모델 학습 및 로드 과정 추가 필요
# #
# #     scaler = StandardScaler()  # 임의의 스케일러 설정
# #     scaler.fit(...)  # 실제 스케일링 학습 데이터 추가 필요
# #
# # except:
# #     print("모델 또는 스케일러를 로드하는 데 문제가 발생했습니다.")
#
# # 사용자가 직접 입력
# new_input = get_user_input(features)
#
# # 예측 점수 계산
# predicted_score = predict_credit_score(new_input, lgb_model, scaler, features)
# print(f"예측된 신용 점수: {predicted_score:.2f}")


############33
#
# def predict_credit_score(input_data, model, scaler, feature_columns):
#     """
#     사용자 입력 데이터를 기반으로 신용 점수를 예측하는 함수.
#
#     Parameters:
#     - input_data (dict): 사용자가 입력한 데이터.
#                          예: {'income': 50000, 'num_cards': 2, ...}
#     - model (LightGBMRegressor): 학습된 LightGBM 모델.
#     - scaler (StandardScaler): 학습에 사용된 스케일러.
#     - feature_columns (list): 모델에 사용된 피처들의 리스트.
#
#     Returns:
#     - predicted_score (float): 예측된 신용 점수.
#     """
#
#     # 입력 데이터를 DataFrame 형태로 변환
#     input_df = pd.DataFrame([input_data])
#
#     # 입력 데이터가 모델의 피처와 동일한 순서를 가지도록 정렬
#     input_df = input_df[feature_columns]
#
#     # 스케일링
#     input_scaled = scaler.transform(input_df)
#
#     # 예측
#     predicted_score = model.predict(input_scaled)
#
#     return predicted_score[0]
#
#
# # 예시 입력값
# new_input = {
#     'income': 50000,  # 연간 소득
#     'num_cards': 2,  # 보유 카드 수
#     'total_loan_amount': 15000,  # 총 대출 금액
#     'loan_duration': 24,  # 대출 기간(개월)
#     # 필요한 다른 피처들 추가...
# }
#
# # 모델에 사용된 feature들의 리스트
# feature_columns =features.columns.tolist()
#
# # 새로운 데이터로 신용 점수 예측
# predicted_score = predict_credit_score(new_input, lgb_model, scaler, feature_columns)
# print(f"예측된 신용 점수: {predicted_score:.2f}")
#
#
