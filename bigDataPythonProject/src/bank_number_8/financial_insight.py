import pandas as pd #Analysis
import numpy as np
import matplotlib.pyplot as plt #Visulization 시각화
import seaborn as sns # 시각 자료 추출에 사용할 seaborn


train = pd.read_csv(r"C:\Users\Administrator\Desktop\82407_KCB_financial_style_data\credit_card_data.csv")
print(train.shape)
print(train.head(5))
print(train.info)

train['city'] = train['city'].fillna('세종')
train['sex'] = train['sex'].fillna('공통')
train['ages'] = train['ages'].apply(lambda x:int(x[:-1])).astype(float)
train['year_month'] = pd.to_datetime((train.year*100+train.month).apply(str),format='%Y%m')
train.drop(['year','month'], axis=1, inplace=True)
train = train[[train.columns[0],'year_month']+list(train.columns[1:-1])]
# pd.set_option('display.max_columns', None)
# print(train.head())

# 사용 카드 수와 신용도 간의 상관관계 시각화
plt.figure(figsize=(10, 6))
sns.scatterplot(x='num_opencard', y='avg_score', data=train)
plt.title('Number of Open Cards vs. AVG_Score')
plt.xlabel('Number of Open Cards')
plt.ylabel('Credit Score')
plt.show()

# 월 할부 금융 대출 금액과 신용도 간의 관계 시각화
# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='monthly_installments_loan', y='avg_score', data=train)
# plt.title('Monthly Installments Loan vs. Credit Score')
# plt.xlabel('Monthly Installments Loan')
# plt.ylabel('Credit Score')
# plt.show()

# 상관계수 계산 OpenCard
correlation = train[['num_opencard', 'avg_score']].corr()
print(correlation)
plt.figure(figsize=(15, 5))

# # 상관계수 계산 UseCard
# correlation = train[['num_usecard', 'avg_score']].corr()
# print(correlation)
# plt.figure(figsize=(15, 5))

# 사용 카드 수와 신용도 간의 관계 시각화
plt.subplot(1, 3, 1)
sns.scatterplot(x='monthly_sbk_loan', y='avg_score', data=train)
plt.title('monthly_sbk_loan vs. Credit Score')
plt.xlabel('monthly_sbk_loan')
plt.ylabel('Credit Score')

# 월은행대출금액과 신용도 간의 관계 시각화
plt.subplot(1, 3, 2)
sns.scatterplot(x='monthly_installments_loan', y='avg_score', data=train)
plt.title('monthly_installments_loan vs. Credit Score')
plt.xlabel('monthly_installments_loan')
plt.ylabel('Credit Score')

# 일시불상환금액과 신용도 간의 관계 시각화
plt.subplot(1, 3, 3)
sns.scatterplot(x='ls_rep_loanb', y='avg_score', data=train)
plt.title('ls_rep_loanb vs. Credit Score')
plt.xlabel('ls_rep_loanb')
plt.ylabel('Credit Score')

plt.tight_layout()
plt.show()

# 상관계수 계산
correlation_num_opencard = train[['monthly_sbk_loan', 'avg_score']].corr()
correlation_monthly_bk_loan = train[['monthly_installments_loan', 'avg_score']].corr()
correlation_is_rep_loanb = train[['ls_rep_loanb', 'avg_score']].corr()

print("monthly_sbk_loan")
print(correlation_num_opencard)
print("\nmonthly_installments_loan")
print(correlation_monthly_bk_loan)
print("\nls_rep_loanb:")
print(correlation_is_rep_loanb)


# 상관계수 계산
correlation_monthly_installments_loan = train[['monthly_installments_loan', 'avg_score']].corr()
print("Correlation between Monthly Installments Loan and Credit Score:")
print(correlation_monthly_installments_loan)

