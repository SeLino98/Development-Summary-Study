import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import shap



# Load the data
train = pd.read_csv(r"C:\Users\Administrator\Desktop\82407_KCB_financial_style_data\credit_card_data.csv")
print(train.head())
print(train.info())

# train.fillna({'city': '세종', 'sex': '공통'}, inplace=True)
# train.fillna(train.mean(), inplace=True)
# Encoding categorical variables
# label_encoder = LabelEncoder()
# train['pop_cd'] = label_encoder.fit_transform(train['pop_cd'])
# train['city'] = label_encoder.fit_transform(train['city'])
# train['sex'] = label_encoder.fit_transform(train['sex'])
# train['age'] = label_encoder.fit_transform(train['age'])

# 예측에 필요없다고 판단되는 컬럼 값들을 버린다. 나이(avg_rat 등)에 경우 너무 상관계수가 높아서 뺌. 의미없는 데이터 또한 제거.
features = train.drop(columns=['avg_score', 'avg_rat', 'population', 'year', 'month', 'ages', 'city', 'pop_cd', 'sex','monthly_bk_loan'])
# features = train.drop(columns=['avg_score', 'avg_rat', 'population', 'year', 'month', 'ages', 'city', 'pop_cd', 'sex', 'num_usecard'])
# 예측 모델 y 종속 변수
target = train['avg_score']

# train과 test 셋 분할
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)



# StandardScaler 작업을 통해 데이터 스케일링
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 모델을 리스트에 담아서 하나씩 돌려보기
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Decision Tree": DecisionTreeRegressor(random_state=42)
}

# 학습 후 각각에 모델에 대해 평가
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f"{name} Model - MSE: {mse}, R^2: {r2}")

# 시각화
rf_model = models['Random Forest']
importance = rf_model.feature_importances_
feature_names = features.columns
indices = np.argsort(importance)
plt.figure(figsize=(10, 8))
plt.title('Feature Importances - DecisionTree ')
plt.barh(range(len(indices)), importance[indices], color='b', align='center')
plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()

# 모델선택
chosen_model = models['Decision Tree']

# SHAP values 계산
explainer = shap.TreeExplainer(chosen_model)
shap_values = explainer.shap_values(X_test)
# SHAP 시각화
shap.summary_plot(shap_values, X_test, feature_names=features.columns) #shap 디폴트 시각 표
shap.summary_plot(shap_values, X_test, feature_names=features.columns, plot_type="bar") #막대플롯을 통해 확인


