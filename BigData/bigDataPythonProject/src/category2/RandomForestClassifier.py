# DecisionTree를 100개 사용하는 앙상블 모델
#DecisionTree에서 과대적합 문제가 발생했을 때 RandomForest를 이용해서 과대적합 문제를 해결할 수도 있다.
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
# n_estimators의 갯수를 늘리거나 max_depth의 숫자를 조절하는 방법으로 성능 조절 가능하다.


model_rf1 = RandomForestClassifier()
# 약하게 예측하기 때문에 과대적합 문제를 해소할 수 있다.
# 예측이 약하니까 안좋은 것아니냐라고 생각할 수 있는데, 해당 부분에 대해선 여러가지의 에측 모델을 통해 더 양을 늘려서 예측하기 때문에
# 예측이 더 좋게 나올 수 있다.

ModelTrain(model_rf1, data)
print(model_rf1.score(X, Y))

model_rf2 = RandomForestClassifier(n_estimators=500) #estimators를 늘릴 수록 높게 나오게 할 수 있다.
ModelTrain(model_rf2, data)
print(model_rf2.score(X, Y))


## 부스팅 방법
from xgboost import XGBClassifier
# 부스팅 방법인데,

model_xgb1 = XGBClassifier()
ModelTrain(model_xgb1, data)
print(model_rf1.score(X, Y))

#### 성능 평가
# 앞서 성능이 좋았던 RandomForestClassifier를 사용하여 모델을 생성합니다.
data = make_sample(seedno=1234, size=50000) # 이번엔 데이터 수를 증분시켜보자.
model_rf = RandomForestClassifier(n_estimators=500)
ModelTrain(model_rf, data)

# 앞서 성능이 좋았던 XGBClassifier를 사용하여 모델을 생성합니다.
data = make_sample(seedno=1234, size=50000)
model_xgb = XGBClassifier(n_estimators=500)
ModelTrain(model_xgb, data)


## 오분류표
# sklearn.metrics.confusion_matrix(y_true, y_pred, *, labels=None, sample_weight=None, normalize=None)
# y_ture: 실제값
# y_pred: 예측값


# RandomForestClassifier의 각 종류별 정확도를 확인해 보도록 합니다.
from sklearn.metrics import confusion_matrix
label=['불합격', '합격']
print(model_rf.score(X, Y))
y_pred = model_rf.predict(X)
a = confusion_matrix(Y, y_pred)
b = pd.DataFrame(a, columns=label, index=label)
b

# XGBClassifier의 각 종류별 정확도를 확인해 보도록 합니다.
# 결과는 RandomforestClassfier 보다 좋게 나오는데, 이상황에선 XGBClassifier 가 더 성능이 좋다는 것을 알 수 있다.

from sklearn.metrics import confusion_matrix
label = ['불합격', '합격']
print(model_xgb.score(X, Y))
y_pred = model_xgb.predict(X)
a = confusion_matrix(Y, y_pred)
b = pd.DataFrame(a, columns=label, index=label)
b

# test 데이터에서 '합격'일 확률에 대한 정보를 저장하여 출력합니다
submission = pd.DataFrame()
submission['id'] = pd.RangeIndex(1, len(X) + 1) # 일련번호를 생성했다.
submission['prob'] = model_xgb.predict_proba(X)[:, 1] # 1일 확률 즉 1번컬러만 합격일 확률만 저장해서
#  model_xgb.predict_proba(X)[:, 1] 이 이제 정답을 제출하는 주요 코드가 된다.
submission.to_csv('submission.csv', index=False)


