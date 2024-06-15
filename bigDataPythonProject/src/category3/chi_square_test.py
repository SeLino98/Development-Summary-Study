# 카이제곱.
# 주 목적. 관측된 데이터가 특정 분포에 잘 맞는지 검사
# 주 목적. 두 범주형 변수 간에 독립성이 있는지 검장.
# 위에 목적을 통해 카이제곱은 크게 3가지로 나눌 수 있다.
# 1. 적합도 : 한 범주형 변수와 귀무 가설에 대해 평가
# 2. 동질성 : 부모 집단에 대해 범주형 변수이 분포가 동질한지 검사
# 3. 독립성 : 두 범주형 변수간 연관성이 있는지 확인
    # H_0 귀무가설 : 기존과 기대가 같다 or 두 변수는 독립이다로 해석할 수 있다

## 01 적합도 검정 : 관측된 데이터가 특정 분포에 잘 맞는지를 검정한다.
    # 귀무 가설 : 데이터는 특정 분포를 따른다.
    # 대립 가설 : 데이터는 특정 분포를 따르지 않는다.
import scipy.stats as stats

# 관측 빈도 (주사위 던지기 결과)
observed = [8, 8, 12, 12, 7, 13]  # 이상적인 공정한 주사위의 결과

# 기대 빈도
expected = [10, 10, 10, 10, 10, 10]  # 기대되는 주사위 결과

# 카이제곱 검정
statistic, p = stats.chisquare(observed, expected)


print(f"Chi2 Statistic: {statistic}, p-value: {p}")
print('귀무가설을 기각' if p < 0.05 else '대립가설 채택')
print('대립가설을 채택하고 \
변수의 분포가 기대 분포와 같지 않다')


## 02 동질성/독립성 검정 :
## 2-1 동질성 검정
# 남 녀에 따라 핸드폰 선호도(Model) 조사
from scipy.stats import chi2_contingency # !! chi2_contingency
import pandas as pd
# 크로스 테이블이 없는 경우 직접 만든다.
cross_table = pd.DataFrame([[10,40,50],[30,60,10]],index=['Man','Female'],columns=["Model_1","Model_2","Model_3"])
chi_statistic,p,df,expected = chi2_contingency(cross_table)
print(f'chi_square:{chi_statistic:.4f}',f'p-value :{p:.4f}',f'df : {df:.4f}',f'expected :\n{pd.DataFrame(expected)}')
print('귀무가설 기각' if p<0.05 else '대립가설 채택')
print('대립가설 : 성별로 핸드폰 모델 선호도 분포가 같지 않다. ')
## 2-2 독립성 검정
# 당뇨 여부와 비만 여부를 조사하고 서로의 관계가 독립인지 검정하자
import pandas as pd
from scipy.stats import chi2_contingency
data = pd.read_csv("")
# 분할표를 직접 만든다.
cross_table2 = pd.crosstab(data['당뇨 여부'],data['비만 여부'])

# 카이스퀘어를 분석한다.
chi_statistic,p,df,expected = chi2_contingency(cross_table2)
print(f'chi 스퀘어 값: {chi_statistic:.4f}',
      f'p-value (0.05): {p:.4f}',
      f'자유도 수: {df}',
      f'기대값:\n{pd.DataFrame(expected)}',
      f'측정값:\n{cross_table2}', sep='\n')
print('기각' if p < 0.05 else '채택')
# [4] 결론
# p > 0.05 이므로, 귀무가설을 채택
# 당뇨와 비만 사이에 관계는 독립이다(연관성이 없다)

