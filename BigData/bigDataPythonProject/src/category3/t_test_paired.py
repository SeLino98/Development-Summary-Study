# t-test에 대한 이해
# 스튜던트 t test라고도 한다.
# 검정 통계량이 귀무가설 하에서 t분포를 따르는 통계적 가설 검정
# 모집단의 표준편차가 알려져 있지 않고, 표본의 크기가 작을 때 유용하다.

# 모집단의 표준편차나 분산이 없을 때 사용하는 방법!
# 검정통계량이 정규 분포를 따르며 모집단의 분산, 표준편차를 알지 못할 때 표본으로 부터 추정된 분산/표준편차를 사용해 검정함
# t-test를 실시하기 위해서는 정규성 및 등분산성의 조건이 만족되어야 함
# 표본을 사용한 모평균 검정 및 두 데이터 세트(집단)의 모평균이 서로 유의하게 다른지 여부를 판별 할 수 있음
# 크게 3가지가 있다.
## 01 독립 표본 t-test (Independent t-test)
## 02 대응 표본 t-test (Paired t-test)
## 03 단일 표본 t-test (one sample t-test)

## 02 대응 표본 t-test (Paired t-test)
'''
동일한 특성을 같는 두집단 A, B의 평균 차이가 유의미한지 확인하는 용도
처치 전/후 비교(효과 검정), 한 집단에 대해 두 가지 방법에 대한 차이 검정 등에 사용
등분산성 검정은 하지 않아도 됨 !!!!!!!!!!!!!
두 약 투여에 따른 추가 수면 시간 평균의 차이가 있는가?
stats.ttest_rel: (two RELated samples)
'''
# 데이터 가져오기
import pandas as pd
df2 = pd.read_csv('./data_02/sleep.csv')
print(df2.shape)
gA = df2.loc[df2.group==1, 'extra']
gB = df2.loc[df2.group==2, 'extra']

from scipy.stats import shapiro
statisticA, pvalueA = shapiro(gA)
statisticB, pvalueB = shapiro(gB)
print(f'statistic: {statisticA:.4f} p-value: {pvalueA:.4f}')
print(f'statistic: {statisticB:.4f} p-value: {pvalueB:.4f}')
# 귀무가설 채택! 정규성을 만족한다

# [Paired t-test]의 정규성 검정
# Paired t-test에서는 전제사항이 대응하는 두 관측값의 차이는 정규 분포를 따라야 한다 입니다.
# 따라서, 아래와 같이 gA-gB 에 대한 정규성 검정한다.
from scipy.stats import shapiro
# 조심하세요 ㅠ.ㅠ  Series의 연산은 index 가 같은 것끼리 연산하는 것입니다.
# index가 서로 다르기 때문에 numpy 값으로 연산해서 사용해야 합니다.
diff = (gA.values - gB.values)
statistic,  pvalue = shapiro(diff)
print(round(statistic, 4))
print(round(pvalue, 4))
print('정규성 만족하지 않음' if pvalue < 0.05 else '정규성 만족')
# 비모수 검정 - Wilcoxon signed rank

from scipy.stats import ttest_rel
statistic, pvalue = ttest_rel(gA, gB, alternative='less')
print(f'statistic: {statistic:.4f} p-value: {pvalue:.4f}')
# statistic: -4.0621 p-value: 0.0014
# statistic이 음수 : gA의 평균이 작고, gB의 평균이 큼




