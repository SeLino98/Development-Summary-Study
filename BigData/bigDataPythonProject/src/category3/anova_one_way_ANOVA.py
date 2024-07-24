# 일원 분산 분석이란
# 범주형인 독립변수 하나와
# 연속형인 종속변수 하나가 있는 것!!
# 독립변수의 변화가 종속변수에 미치는 영향을 보기 위해 사용한다.
# 정규성을 만족하고 등분산성과 독립성을 만족해야 한다

import pandas as pd
iris = pd.read_csv('bigdata/iris')
iris.columns = ['sepal_length', 'sepal_width',
                'petal_length', 'petal_width', 'target']

# [2-1] 품종별 각 변수의 평균 확인
iris.groupby('target').mean()

# [2-2] 특정 변수에 대한 품종별 평균 확인
feature = 'sepal_width'
iris.groupby('target')[feature].mean()

# group 0, 1, 2의 평균의 차이가 있습니다
# 평균값의 차이가 ""실제로"" 의미가 있는 차이인지 알고 싶다면, 분산 분석을 통해 통계적 유의성을 알아 볼 수 있다.
# 통계적 의미가 있는지 차이를 알고 싶다면, 분산 분석Anova를 통해 통계적 유의성을 알아 볼 수 있다.

# [4] 정규성 확인
# p-value가 0.05 보다 큰 값일 때 정규성을 갖음
from scipy.stats import shapiro
data = [x[1].values for x in iris.groupby('target')[feature]]
print(data)
_, pvalue0 = shapiro(data[0])
_, pvalue1 = shapiro(data[1])
_, pvalue2 = shapiro(data[2])
print(f'{pvalue0:.4f} {pvalue1:.4f} {pvalue2:.4f}')

# [5] 등분산성 확인
# p-value가 0.05 보다 큰 값일 때 등분산성을 갖음
from scipy.stats import bartlett
#_, pvalue = bartlett(data[0], data[1], data[2])
_, pvalue = bartlett(*data)
print(f'{pvalue:.4f}')

# [6] 일원분산분석 - 1번째 방법
from scipy.stats import f_oneway
F, pvalue = f_oneway(*data)
print(f'iris 데이터의 일원분산분석 결과 : F={F}, p={pvalue}')
if pvalue < 0.05:
    print('P-value 값이 충분히 작음으로 인해 \
그룹의 평균값이 통계적으로 유의미한 차이가 있음')

# [7] 일원분산분석 - 2
import statsmodels.api as sm
from statsmodels.formula.api import ols
data = iris[['target', 'sepal_width']]
lm = ols('sepal_width ~ C(target)', data).fit()
result = sm.stats.anova_lm(lm)
print(result)

# [7] 일원분산분석 - 2 (이렇게 하면 더 편합니다!) from_formula사용
# module import 방법 변경해 보았습니다.
from statsmodels.api import OLS
from statsmodels.stats.anova import anova_lm
data = iris[['target', 'sepal_width']]
lm = OLS.from_formula('sepal_width ~ C(target)', data).fit()
result = anova_lm(lm)
print(result)
'''
              df     sum_sq   mean_sq         F        PR(>F)
C(target)    2.0  11.344933  5.672467  49.16004  4.492017e-17
Residual   147.0  16.962000  0.115388       NaN           NaN
'''

iris['sepal_width'].var() #0.189979418344519

# C(target)의 PR(=p-value) 값이 0.05 보다 작으므로 그룹의
# 평균값이 통계적으로 유의미하게 차이가 있음
# 구체적으로 어떤 집단이 차이가 있는지 확인하려면
# 사후분석(post hoc tests)를 해야함
# 유의미한 차이가 없는 경우는 사후분석할 필요가 없음
### 사후검정(Post Hoc Analysis)
#
# ANOVA 분석의 문제 : 다르다는 것은 알지만, 어떤 집단간의 차이가 있는지는 알 수 없음
# 사후검정을 통해 어떤 것에 차이가 있는지 찾을 수 있음
# post hoc은 라틴어로 "after this"의 뜻
# 사후검정의 종류
# Tukey's HSD (Honest Significant Difference) test : 정규분포, 등분산, 동일 표본 크기에서 가장 많이 사용
# Duncan’s new multiple range test (MRT) : 정규분포, 등분산, 동일 표본 크기에서 사용, 엄격하지 않은 기준으로 통계적 유의성을 도출하기 쉬움
# Scheffé’s Method : 가장 보수적이고 엄격한 사후검정방식 (동일하지 않은 표본 크기)
# 민감도(sensitivity)로 구분 : Scheffe < Tukey < Duncan/Fisher
# Duncan의 방법은 작은 차이에도 차이가 난다라고 하지만, Scheffe의 방법은 확실한 차이가 나야만 비로소 차이가 있다라고 판단함

'''

ANOVA(Analysis of Variance)는 두 개 이상의 그룹 간의 평균 차이를 분석하기 위해 사용되는 통계적 기법입니다. ANOVA를 사용하는 주된 이유는 다음과 같습니다:

여러 그룹 비교: ANOVA는 두 개 이상의 그룹 간의 평균 차이를 비교할 때 유용합니다. t-검정은 두 그룹 간의 비교만 가능하지만, ANOVA는 여러 그룹을 동시에 비교할 수 있습니다.

통계적 유의성 평가: ANOVA는 그룹 간의 차이가 우연에 의한 것인지, 아니면 실제로 유의미한 차이인지를 평가할 수 있습니다. 이는 p-값을 통해 결정됩니다.

요인 효과 평가: ANOVA는 단일 요인(일원분산분석, One-Way ANOVA) 또는 다중 요인(이원분산분석, Two-Way ANOVA 등)을 평가할 수 있어, 각 요인이 결과 변수에 미치는 영향을 파악할 수 있습니다.

상호작용 효과 분석: 이원분산분석과 같은 다중 요인 ANOVA는 요인 간의 상호작용 효과를 분석할 수 있어, 복잡한 데이터의 관계를 더 잘 이해할 수 있습니다.

모델 적합성 평가: ANOVA는 회귀 분석 모델의 적합성을 평가하고, 독립 변수들이 종속 변수에 미치는 영향을 확인할 때 사용됩니다.

데이터의 분산 파악: ANOVA는 데이터의 총 변동을 그룹 내 변동과 그룹 간 변동으로 나누어 분석함으로써, 각 그룹이 얼마나 변동이 있는지를 파악할 수 있습니다.

ANOVA 분석을 통해 연구자는 여러 그룹 간의 평균 차이를 체계적으로 비교하고, 그 차이가 통계적으로 유의미한지 여부를 평가할 수 있습니다. 이는 다양한 연구 및 실험에서 매우 중요한 역할을 합니다.
'''



