import pandas as pd
''' 1번 문제 
A 회사에서 판매하는 모니터는 평균 5개 보다 적은 불량화소를 포함한다고 주장한다. 이 주장을 판단하기 위해서 데이터를 수집했으며, 주어진 데이터(data_02/defective.csv)에는 모니터 25개에서 조사한 불량화소 개수가 저장되어 있다.

불량화소의 개수는 정규분포를 따른다고 할 때, 이 주장의 타당성 여부를 유의수준 5%에서 검정하여라
𝑯_𝟎 : 𝝁≥𝟓, 𝑯_𝟏 : 𝝁<𝟓, defective_pixel : 불량화소 개수
(a) 불량화소의 표본 평균을 구하시오 (반올림하여 소수 둘째자리까지 계산)
(b) 위의 가설을 검정하기 위한 검정통계량을 입력하시오.(반올림하여 소수 넷째자리까지 계산)
(c) 위의 통계량에 대한 p-값을 구하여 입력하시오. (반올림하여 소수 넷째자리까지 계산)
(d) 유의수준 0.05 하에서 가설검정의 결과를 (채택/기각) 중 하나를 선택하여 입력하시오.
'''
##적은 걸 주장한다?
# 귀무가설은 불량화소의 개수는 5개보다 같거나 많다.
# 대립가설은 불량화소의 개수가 5개보다 적다
# alternative를 less로 설정한다.
import pandas as pd
from scipy.stats import ttest_1samp #1개의 샘플
from scipy.stats import ttest_rel, ttest_ind
from sklearn.tree import DecisionTreeClassifier ,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor

data = pd.read_csv('data_02/defective.csv')
answer_a = round(data['defective_pixel'].mean(),2)
print(answer_a)
popmean = 5
statistic,p_value = ttest_1samp(data['defective_pixel'], popmean, alternative="less")

answer_b = round(statistic,4)
answer_c = round(p_value,4)
print(answer_b)
print(answer_c)

print('귀무가설 기각' if p_value < 0.05 else '귀무가설 채택')
# 4.84
# -1.4446
# 0.0807
# 채택
''' 2번 문제
주어진 데이터(data_02/blood_pressure.csv)에는 고혈압 환자 120명의 치료 전후의 혈압이 저장되어 있다. 해당 치료가 효과가 있는지 (즉, 치료 후의 혈압이 감소했는지) 쌍체표본 t-검정(paired t-test)를 통해 답하고자 한다. 가설은 아래와 같다
𝑯_𝟎 : 𝝁_𝒅≥𝟎, 𝑯_𝟏 : 𝝁_𝒅<𝟎 (𝝁_𝒅 : 치료 후 혈압 – 치료 전 혈압)의 평균
bp_before : 치료 전 혈압, bp_after : 치료 후 혈압
(a) ud의 표본 평균을 구하시오 (반올림하여 소수 둘째자리까지 계산)
(b) 위의 가설을 검정하기 위한 검정통계량을 입력하시오.(반올림하여 소수 넷째자리까지 계산)
(c) 위의 통계량에 대한 p-값을 구하여 입력하시오. (반올림하여 소수 넷째자리까지 계산)
(d) 유의수준 0.05 하에서 가설검정의 결과를 (채택/기각) 중 하나를 선택하여 입력하시오.
'''
from scipy.stats import ttest_rel
# 문제에 가설을 봤을 때
# 귀무가설은 치료 후 혈압과 치료 전 혈압의 차가 0보다 크거나 같다.
# 대립가설은 그의 반대 후와 전의 차가 0보다 작다. 즉 alternative를 less로 설정한다.
data = pd.read_csv('data_02/blood_pressure.csv')
print(data.head(5))
## 표본 평균을 구하기
data['ud'] = data['bp_after']-data['bp_before']
answer_a = round(data['ud'].mean(),2)
print(answer_a)
statistic,p_value = ttest_rel(data['bp_after'],data['bp_before'],alternative='less')
answer_b = round(statistic,4)
print(answer_b)
answer_c = round(p_value,4)
print(answer_c)
print('귀무가설 기각' if p_value <0.05 else '귀무가설 채택')