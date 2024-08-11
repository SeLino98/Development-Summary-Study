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
features = train.drop(columns=['avg_score', 'avg_rat', 'population', 'year', 'month', 'ages', 'city', 'pop_cd', 'sex','monthly_cd_loan','monthly_insurance_loan'])
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
lgb_model = lgb.LGBMRegressor(n_estimators=5000,learning_rate=0.3)
lgb_model.fit(X_train, y_train)

# 예측 및 평가
predictions = lgb_model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f"LightGBM Model - MSE: {mse}, R^2: {r2}")

# 시각화
importance = lgb_model.feature_importances_
feature_names = features.columns
indices = np.argsort(importance)
plt.figure(figsize=(10, 8))
plt.title('Feature Importances - LightGBM')
plt.barh(range(len(indices)), importance[indices], color='b', align='center')
plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()

# SHAP values 계산
explainer = shap.TreeExplainer(lgb_model)
shap_values = explainer.shap_values(X_test)

# SHAP 시각화
shap.summary_plot(shap_values, X_test, feature_names=features.columns)  # SHAP 디폴트 시각 표
shap.summary_plot(shap_values, X_test, feature_names=features.columns, plot_type="bar")  # 막대 플롯으로 확인


