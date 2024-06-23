
from scipy.stats import shapiro, bartlett
# 둘 다 리턴이 statsm, pvalue
# shapiro 는 정규성
# bartlett 은 등분산성

from scipy.stats import chi2_contingency ,chisquare

# 둘 다 크로스테이블 만들어야 됨.
# chisquare은 확률 테이블 넣어줘야됨 .
# 4개 값 리턴

from scipy.stats import ttest_ind,ttest_1samp,ttest_rel
# alternative
# statistic, p_value

from statsmodels.api import OLS,Logit
model = OLS.from_formula('weight ~ age + cholesterol',df).fit()
result = model.params['age'] # 회귀 계수
result2 = model.pvalues['cholesterol'] # p
# model.rsquared 결정계수

# 둘 다 모델 값을 받음
# 가능하면 from_formula를 사용하기
# 독립이 범주형일 경우 C()



