from scipy.stats import hypergeom

a, b, c = 28, 8, 5
result = round(1 - hypergeom(M=a, n=b, N=c).cdf(1), 4)
print(result)

from scipy.stats import hypergeom

a, b, c = 40, 10, 4
result = round(hypergeom(M=a, n=b, N=c).pmf(3), 4)
print(result)

# 포아송 분포
# 단위 시간이나 단위 공간에서 어떤 사건이 몇 번 발생할 것인지를 표현하는 분포
# 단위 시간 또는 단위 공간 내에서 발생하는 사건의 발생횟수에 따른 확률을 구할 때 사용
#	확률을 구하기 위해 사건의 평균과 발생횟수를 알아야 한다.
#	단위에 대한 부분을 조심할 것
# ex ) 어느 AS 센터에 1시간당 평균 180 건의 전화가 온다
# 1분 동안 걸려오는 전화 요청이 4건 이하일 확률은 ??

# 6페이지에서 오타가 총 12개일 때
# 한페이지를 검수할 때 오타가 2개 나올 확률

# 12/6 = 2 해서 mu = 2 이다.


from scipy.stats import poisson

mu = 8
result = 1 - poisson(mu=mu).cdf(5)
print(round(result, 4))

from scipy.stats import poisson

mu = 2
result = poisson(mu=mu).pmf(2)
print(round(result, 4))

## 연속형 확률 분포 - 정규 분포 (normal distrubuttion )
# - 가우스 분포라고도 한다. 평균과 표준편차에 대해 모양이 결정되고 N(u,v)로 표기
# - 평균 0, 표준편차/ 분산 1 인 정규 분포 를 표준 정규 분포이자 Z 분포라고 한다.
# - 키 몸무게 , 시험 점수 등 거의 대부분의 측정값이 정규분포를 따른다.
# Normal 정규 분포 객체 생성
# from scipy.stats import norm
# loc = 평균
# scale = 표준편차
# norm(loc = 0, scale = 1)
# pdf는 확률 밀도 함수
# cdf는 누적 밀도 함수
# ppf 는 표본 오차나 신뢰도 등을 구할 때 사용
# ppf는 확률 값을 주면 그때의 x 값을 준다.
# confidence 확률 값, 신뢰도


# 표준정규분포 객체 생성 및 그래프 그리기 - loc, scale 대응
from scipy.stats import norm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mloc, mscale = 0, 1

rv = norm(loc=mloc, scale=mscale)  # loc=평균, scale=표준편차
x = np.arange(mloc-8*mscale, mloc+8*mscale, 0.1)  # 4표준편차 범위로 지정
y1 = rv.pdf(x)
y2 = norm.pdf(x, loc=mloc, scale=mscale*0.5)
y3 = norm.pdf(x, loc=mloc, scale=mscale*2)
df = pd.DataFrame()
df[f'normal_{mscale}'] = pd.Series(y1, index=x)
df[f'normal_{mscale*0.5}'] = pd.Series(y2, index=x)
df[f'normal_{mscale*2}'] = pd.Series(y3, index=x)
df.plot(title='Normal PDF', figsize=(5, 3), grid=True)
plt.show()



## t 분포
# 정규분포는 표본의 수가 적으면 신뢰도가 낮아진다. (n이 30 미만일 경우!! )
# 때문에 표본을 많이 봅지 못하는 경우에 대한 대응책으로 예측 범위가 넓은 분포를 사용하며
# 이것이 t-분포이다.

# t분포는 표본의 개수에 따라 그래프의 모양이 변한다.
# 표본의 개수가 많아질수록 정규분포와 비슷하다
# 표본의 개수가 적을수록 신뢰도가 낮아지기 때문에 예측 범위를 넓히기 위해 옆으로 퍼지게 된다.
# t분포는 표본의 개수가 30개 미만일 때 사용하며, 신뢰구간 가설검정에 사용한다.
# 그래프의 x 축 좌표를 t 값이라고 부르며 t값을 사용해 p-value를 구하게 된다.



# Z회사의 USB 수명을 조사하였더니 USB의 평균 수명은 5000시간이고, 표준편차가 100시간인 정규분포를 따른다고 한다. USB의 수명이 4800시간 이하일 확률을 구하시오
from scipy.stats import norm

loc = 5000
scale = 100
usb_limits = 4800
result = norm(loc,scale).cdf(usb_limits)
result = round(result,4)
print(result)


from scipy.stats import norm

mu = 10
scale = 2
refriger_limits = 14

result = round(1 - norm(mu,scale).cdf(refriger_limits),4)

print(result)

# X회사에서 생산되는 계란은 평균 무게가 80g 이고 분산이 100g인 정규분포를 따른다고 한다. 계란의 평균 무게가 55g ~ 90g일 확률을 구하시오.
from scipy.stats import norm
import math

mu_egg_weight = 80
scale = 100 ** 0.5 # -> 분산값이 100으로 주어졌기 때문에 scale(표준편차) 값으로 바꿔줘야 한다. **0.5를 통해 구해주자
scale = math.sqrt(100) # 아니면 math 값을 받아서 사용해보자 .

start_egg_weight = 55
end_egg_weight = 90
per =  norm(mu_egg_weight,scale).cdf(end_egg_weight) - norm(mu_egg_weight,scale).cdf(start_egg_weight)
result = round(per,4)
print(result)






