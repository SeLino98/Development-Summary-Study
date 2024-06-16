
## 등분산성

# 주 라이브러리
# burtlett : 데이터셋의 크기가 서로 다른 2개 이상의 집단 사용 가능
# levene, fligner : 정규성을 충족하지 않은 비모수 데이터에 대해서도 사용가능
import pandas as pd
from scipy.stats import shapiro
from scipy.stats import bartlett
iris = pd.read_csv('iris') #붓꽃
target = 'sepal_length'
group_a = iris.loc[iris['species']=='setosa',target].to_list()
group_b = iris.loc[iris['species']=='versicolor',target].to_list()
group_c = iris.loc[iris['species']=='virginica',target].to_list()

''' print(group_a,b,c)
[5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7, 5.1, 5.4, 5.1, 4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4, 5.1, 5.0, 4.5, 4.4, 5.0, 5.1, 4.8, 5.1, 4.6, 5.3, 5.0]
[7.0, 6.4, 6.9, 5.5, 6.5, 5.7, 6.3, 4.9, 6.6, 5.2, 5.0, 5.9, 6.0, 6.1, 5.6, 6.7, 5.6, 5.8, 6.2, 5.6, 5.9, 6.1, 6.3, 6.1, 6.4, 6.6, 6.8, 6.7, 6.0, 5.7, 5.5, 5.5, 5.8, 6.0, 5.4, 6.0, 6.7, 6.3, 5.6, 5.5, 5.5, 6.1, 5.8, 5.0, 5.6, 5.7, 5.7, 6.2, 5.1, 5.7]
[6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2, 6.5, 6.4, 6.8, 5.7, 5.8, 6.4, 6.5, 7.7, 7.7, 6.0, 6.9, 5.6, 7.7, 6.3, 6.7, 7.2, 6.2, 6.1, 6.4, 7.2, 7.4, 7.9, 6.4, 6.3, 6.1, 7.7, 6.3, 6.4, 6.0, 6.9, 6.7, 6.9, 5.8, 6.8, 6.7, 6.7, 6.3, 6.5, 6.2, 5.9]
'''

#등분산성 검정을 하기 전에 정규성 검정을 한다.
a_statistic,p_a = shapiro(group_a)
b_statistic,p_b = shapiro(group_b)
c_statistic,p_c = shapiro(group_c)
print(p_a,p_b,p_c) # 해당 조건 모두 귀무가설을 채택하는지 확인한다.

# 귀무가설이 채택된 가설들에 대해 등분산성 검정을 실행한다.
# 등분산성 검정
statistic,p_value = bartlett(group_a,group_b,group_c)

## 정규성을 만족하지 않은 비모수 데이터에 대해서 사용가능한 levene와 fliger 가 있다.

# levene 의 center는 'mean'으로 지정
groups = [x.to_list() for name, x in iris.groupby('species')[target]]
print(groups)
gA, gB, gC = groups
print(gA)

from scipy.stats import levene
statistic, pvalue = levene(*groups, center='mean')
print(statistic, pvalue)
# 귀무가설 기각 - 등분산성 만족하지 않음

# fligner의 center는 'trimmed', proportiontocut=5% 지정
from scipy.stats import fligner
statistic, pvalue = fligner(*groups, center='trimmed',
                            proportiontocut=0.05)
print(statistic, pvalue)
# 귀무가설 기각 - 등분산성 만족하지 않음.

