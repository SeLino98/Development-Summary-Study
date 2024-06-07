
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
help(DecisionTreeClassifier)

#DessionTree는 오버피팅 경향이 있다.
# 때문에 max_depth를 줄이면서 overfitting을 해결한다.


model_dc1 = DecisionTreeClassifier()
ModelTrain(model_dc1, data)
print(model_dc1.score(X, Y))

model_dc2 = DecisionTreeClassifier(max_depth=6) # max_depth를 줄이면 성능이 떨어지는데, 분리를 할 수 있는만큼 한 것이 아니라, 중간에 멈췄기 때문에
# 멈췄을 땐 과대적합이 생겼을 때 max_depth를 조절해서 train과 test 성능을 맞춰 과대적합 문제를 해결한다.

ModelTrain(model_dc2, data)
print(model_dc2.score(X, Y))

model_dc3 = DecisionTreeClassifier(max_depth=3)
ModelTrain(model_dc3, data)
print(model_dc3.score(X, Y))




