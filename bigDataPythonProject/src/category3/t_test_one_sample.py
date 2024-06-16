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


## 03 단일 표본 t-test ( one sample이므로 등분산 검정 필요 없음 )
# 사용 시기: 하나의 그룹의 평균이 특정 값과 다른지를 비교할 때 사용합니다. 예를 들어, 특정 지역 학생들의 시험 점수가 전국 평균보다 높은지 여부를 확인하는 경우.

# 20대 수면시간이 전체의 수면시간의 평균같인지 아닌지 확인하기
# 가장 먼저 20대의 수면시간에 대해 정규성 검정
# one sample이므로 등분산 검정 필요 없음
import pandas as pd

df = pd.read_csv("./data_02/sleepage.csv")
print(df.shape)

from scipy.stats import shapiro
statistic, pvalue = shapiro(df['stime20s'])
print(round(statistic, 4), round(pvalue, 4))
print('기각' if pvalue < 0.05 else '채택')
# 귀무가설 : 정규성을 만족한다.
# 20대의 수면시간에 대해 평균 구하기
sleep = df['stime20s'].mean()
print(round(sleep, 4), f'{sleep :.04f}')

# 이제 t-test를 임포트 해서 사용해보자 .
from scipy.stats import ttest_1samp
popmean = 6 # 평균 시간이 6시간
statistic, p_value = ttest_1samp(df['stime20s'],popmean,alternative='two-sided')

# 가설 결과
# p-value 가 0.05보다 크다.!! 즉 귀무가설을 채택해야한다
# 귀무가설을 채택하기 때문에 20대 수면시간의 평균은 6시간이 이다
print('기각' if pvalue < 0.05 else '채택')


# 만약 alternative = 'less', alternative = 'greater' 라면 ?
# less의 경우 20대 수면시간의 평균이 6시간 보다 작다. 라고 되는것이고
# greater의 경우 20대 수면시간의 평균이 6시간 보다 크다. 라고 되는 경우로 가설이 생성이되는 경우이다,










