import pickle
import light_gbm as lg
import pandas as pd


def predict_credit_score(input_data, model, scaler, feature_columns):
    """
    사용자 입력 데이터를 기반으로 신용 점수를 예측하는 함수.

    Parameters:
    - input_data (dict): 사용자가 입력한 데이터.
                         예: {'income': 50000, 'num_cards': 2, ...}
    - model (LightGBMRegressor): 학습된 LightGBM 모델.
    - scaler (StandardScaler): 학습에 사용된 스케일러.
    - feature_columns (list): 모델에 사용된 피처들의 리스트.

    Returns:
    - predicted_score (float): 예측된 신용 점수.
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


# 예시 입력값
new_input = {
    'income': 50000,  # 연간 소득
    'num_cards': 2,  # 보유 카드 수
    'total_loan_amount': 15000,  # 총 대출 금액
    'loan_duration': 24,  # 대출 기간(개월)
    # 필요한 다른 피처들 추가...
}

# 모델에 사용된 feature들의 리스트
feature_columns =lg.features.columns.tolist()

# 새로운 데이터로 신용 점수 예측
predicted_score = predict_credit_score(new_input, lg.lgb_model, lg.scaler, feature_columns)
print(f"예측된 신용 점수: {predicted_score:.2f}")
