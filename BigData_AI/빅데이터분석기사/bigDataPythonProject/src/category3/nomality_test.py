

## 모수검정에는 비율과 등간이 있다/
## 여기서 가장 먼저 정규성을 갖는지 확인읋 하고
## 그 다음의 등분산성을 갖는지 확인을 하면서 나눠서 그에 따른 검정 방법을 실시하면 된다 .

## 01정규성 검정
## 말그대로 해당 데이터 셋이 정규분포를 따르는지 귀무 대립 가설을 설정하고 p-value 값을 이용해서 검정하는 방법이다.
import pandas as pd
import numpy as np
df = pd.read_csv('')
# 각각의 그룹들이 정규성을 갖는지 확인한다.
group_a = df['stime20s']
group_b = df['stime40s']

from scipy.stats import shapiro ## 정규성을 갖는지에 대한 검정통계량과 p 밸류 값을 준다
A_statistic, a_p = shapiro(group_a)
B_statistic, b_p = shapiro(group_b)

#만약 유의 수준이 0.05 일 때
print(f'그룹A: 검정통계량: {A_statistic:.4f}, p-value: {a_p:.4f}')  # 정규성 만족
print(f'그룹B: 검정통계량: {B_statistic:.4f}, p-value: {b_p:.4f}')  # 정규성을 만족하지 않음
# 으로 결과를 가져올 수 있다.


## 데이터 양이 많을 땐 정규성 검정에서 kstest를 사용한다.
from scipy.stats import kstest, norm
a_statistic,p_a = kstest(group_a,norm.cdf)
b_statistic, p_b = kstest(group_b, norm.cdf)

print(f'그룹A: 검정통계량: {A_statistic:.8f}, p-value: {a_p:.8f}')  # 정규성을 만족하지 않음
print(f'그룹B: 검정통계량: {B_statistic:.8f}, p-value: {b_p:.8f}')  # 정규성을 만족하지 않음































