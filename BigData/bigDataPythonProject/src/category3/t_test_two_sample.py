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


## 01 Independent t-test ( Two Sample t-test )
'''
두집단 A, B의 평균 차이가 유의미한지 확인하는 용도
20대와 40대의 수면 시간은 같다
stats.ttest_ind : (two INDependent sample이라 해서 ttest_ind )
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
t값과 two-tail p-value를 반환함
ttest_ind(a, b, equal_var=False) : Welch's t-test 수행 (등분산이 아닌 경우)
'''
# 수면 시간 정보가 포함된 파일 불러오기
import pandas as pd
df2 = pd.read_csv('./data_02/sleepage.csv')
print(df2.shape)
group_a = df2.loc[:,'stime20s']
group_b = df2.loc[:,'stime40s']

# 등분산 검정 - 3가지 방법으로 실행 후, pvalue 확인
from scipy.stats import levene, fligner, bartlett
from scipy.stats import shapiro

# 정규성 검정
statistic, pvalueA = shapiro(group_a)  # 정규성 만족         0.1180
statistic, pvalueB = shapiro(group_b)  # 정규성 만족하지 않음 0.0184
print(f'{pvalueA:.04f}, {pvalueB:.04f}')

# 등분산성 검정
statisticA, pvalueA = levene(group_a, group_b)    # 등분산성 만족
statisticB, pvalueB = fligner(group_a, group_b)   # 등분산성 만족
statisticC, pvalueC = bartlett(group_a, group_b)  # 등분산성 만족
print(f'{pvalueA:.04f}, {pvalueB:.04f}, {pvalueC:.04f}')

# two-sample t-test 수행
from scipy.stats import ttest_ind
statistic, pvalue = ttest_ind(group_a, group_b, alternative='two-sided')
print(f'statistic: {statistic:.04f}, pvalue: {pvalue:.04f}')

### !! 이것도 one sample ttest 처럼
# less greate two-side가 있는데
## 각각은 다음과 같다.
''' # greater
alternative='greater'
귀무가설 : groupA의 평균 - groupB의 평균이 0보다 작거나 같다
대립가설 : groupA의 평균 - groupB의 평균이 0보다 크다
귀무가설 : groupA의 평균이 groupB의 평균보다 작거나 같다
대립가설 : groupA의 평균이 groupB의 평균보다 크다
'''
''' # less
alternative='less'
귀무가설 : groupA의 평균 - groupB의 평균이 0보다 크거나 같다
대립가설 : groupA의 평균 - groupB의 평균이 0보다 작다
귀무가설 : groupA의 평균이 groupB의 평균보다 크거나 같다
대립가설 : groupA의 평균이 groupB의 평균보다 작다
'''
''' # two-sided
alternative='two-sided'
귀무가설 : groupA의 평균 - groupB의 평균이 0과 같다
대립가설 : groupA의 평균 - groupB의 평균이 0과 같지 않다
귀무가설 : groupA, groupB의 평균은 동일하다
대립가설 : groupA, groupB의 평균은 동일하지 않다
'''

















