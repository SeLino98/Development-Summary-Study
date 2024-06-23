### 이원 분산 분석
# 독립변인(범주형)의 수가 두 개일 때 집단 간 종속변수(연속형)의 평균 차이가 유의한지를 검증하는 데 사용
# 상호작용효과(Interaction effect) 즉, 한 독립변수의 변화가 결과에 미치는 영향이 다른 독립변수의 수준에 따라 달라지는지를 확인하기 위해 사용됨
# statsmodels 라이브러리를 이용

# 데이터 가져오기
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/data_02/main/altman.csv')
data.tail()


# 태아별 머리 둘레 평균을 구해보자
data.groupby('fetus')['head_size'].mean()
'''
fetus
1.0    13.991667
2.0    19.691667
3.0    12.825000
Name: head_size, dtype: float64
'''

#3개의 집단에 대해 머리 둘레가 차이가 있어 보인다.
# 이원 분산 분석을 통해 정확하게 상호작용이 어떤지 확인해보자.
# 이원 분산의 경우 다음과 같이 가설을 세울 수 있다.
# 귀무가설 : 측정자별 머리둘레 평균은 동일하다
# 대립가설 : 측정자별 머리둘레 평균은 동일하지 않다 (차이가 있다)
# 귀무가설 : 태아별 머리둘레 평균은 동일하다
# 대립가설 : 태아별 머리둘레 평균은 동일하지 않다 (차이가 있다)
# 귀무가설 : 머리둘레평균에 대해 측정자와 태아에 상호작용 효과가 없다 (독립이다, 영향을 주지 않는다)
# 대립가설 : 머리둘레평균에 대해 측정자와 태아에 상호작용 효과가 있다 (독립이 아니다, 영향을 준다)


# 이원 분산 분석
from statsmodels.formula.api import ols
from statsmodels.api import OLS
from statsmodels.stats.anova import anova_lm

# [1] 분산 분석표 반환 - 교호작용 불포함
#model = ols('head_size ~ C(fetus) + C(observer)', data).fit()
model = OLS.from_formula('head_size ~ C(fetus) + C(observer)', data).fit()
result = anova_lm(model)
print(result)
# 평균
# df, sum_sq, mean_sq, F, PR(>F)
# Residual (잔차)
# 결정계수(r2), mse

'''C(fetus) + C(observer)의 두 범주형 데이터에서  PR을 통한 4개의 귀무 가설을 알 수 있다. 
               df      sum_sq     mean_sq            F        PR(>F)
C(fetus)      2.0  324.008889  162.004444  2023.182239  1.006291e-32
C(observer)   3.0    1.198611    0.399537     4.989593  6.316641e-03
Residual     30.0    2.402222    0.080074          NaN           NaN
'''


from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
# [0] 머리둘레 데이터 - 태아, 관찰자
data = pd.read_csv('https://raw.githubusercontent.com/Soyoung-Yoon/data_02/main/altman.csv')

# [1] 분산 분석표 반환 - 교호작용 포함(독립변수끼리 서로 영향을 미치는지, 상호작용) 서로 연관성이 있는지 알아보자.
model = ols('head_size ~ C(fetus) + C(observer) + C(fetus):C(observer)', data).fit()
result = anova_lm(model)
print(result)
'''
                        df      sum_sq     mean_sq            F        PR(>F)
C(fetus)               2.0  324.008889  162.004444  2113.101449  1.051039e-27
C(observer)            3.0    1.198611    0.399537     5.211353  6.497055e-03
C(fetus):C(observer)   6.0    0.562222    0.093704     1.222222  3.295509e-01
Residual              24.0    1.840000    0.076667          NaN           NaN
'''

# C(fetus):C(observer) : 교호 작용 포함하여 독립변수끼리 영향이 있는지 알아 봤는데,
# C(fetus):C(observer)의 P-value 가 0.05 이상이다.
# 따라서 귀무가설을 기각할 수 없고.
# 머리둘레평균에 대해 측정자와 태아에 상호작용 효과가 없다.




