import pandas as pd #Analysis
import numpy as np
import matplotlib.pyplot as plt #Visulization 시각화
import seaborn as sns # 시각 자료 추출에 사용할 seaborn
# import warnings
# from lightgbm import LGBMRegressor
# from xgboost import XGBRegressor
# import eli5
# from eli5.sklearn import PermutationImportance
# import shap
# plt.rcParams["figure.facecolor"] = 'w'
# plt.rcParams["font.family"] = 'NanumBarunGothic'
# plt.rcParams['axes.unicode_minus'] = False


# CSV  파일 경로
# C:\Users\Administrator\Desktop\82407_KCB_financial_style_data\credit_card_data
# C:\Users\Administrator\Desktop\82407_KCB_financial_style_data\jeju_financial_life_data
train = pd.read_csv(r"C:\Users\Administrator\Desktop\82407_KCB_financial_style_data\credit_card_data.csv")
print(train.shape)
print(train.head(5))
print(train.info)

## 결측치를 확인해본다.
missing_values = train.isnull().sum()
print(missing_values)
total_missing = train.isnull().sum().sum()
print(f"Total missing values: {total_missing}") # 결측치 값의 총 갯수를 확인
has_missing_values = train.isnull().values.any()
print(f"Any missing values? {has_missing_values}") # 결측치 값이 있는지 확인
# sns.heatmap(train.isnull(), cbar=False, cmap='viridis')
# plt.show() # 결측치에 대한 시각 자료

train['city'] = train['city'].fillna('세종')
train['sex'] = train['sex'].fillna('공통')
train['ages'] = train['ages'].apply(lambda x:int(x[:-1])).astype(float)
train['year_month'] = pd.to_datetime((train.year*100+train.month).apply(str),format='%Y%m')
train.drop(['year','month'], axis=1, inplace=True)
train = train[[train.columns[0],'year_month']+list(train.columns[1:-1])]
# pd.set_option('display.max_columns', None)
# print(train.head())


unique_counts = train.nunique() # 종류 갯수
print(unique_counts)
from sklearn.preprocessing import LabelEncoder
### 상관관계 분석하기
#데이터 컬럼 사이의 상관관계를 계산해 비례함의 정도를 보인다.
# 양의 상관관계가 클수록 비례관계, 음의 상관관계가 클수록 반비례 관계,  0에 가까우면 서로 독립으로 볼 수 있다.
# Initialize LabelEncoder
label_encoder = LabelEncoder()
train['pop_cd'] = label_encoder.fit_transform(train['pop_cd'])
train['city'] = label_encoder.fit_transform(train['city'])
train['sex'] = label_encoder.fit_transform(train['sex'])
numeric_cols = train.select_dtypes(include=[np.number])
print(numeric_cols.columns)  # Optional: print the numeric column names to verify
corr = train.corr(method='pearson', min_periods=1)
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# 시각자료 도출
sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.show()
# corr = train.corr().unstack().sort_values(ascending=False).drop_duplicates().drop_duplicates()
# corr.drop(corr.index[0],inplace=True)
# display(corr.head())
# display(corr.tail(5))

corr = train.corr().unstack().sort_values(ascending=False).drop_duplicates().drop_duplicates()
corr.drop(corr.index[0],inplace=True)
print(corr.head())
print(corr.tail(5))

corr = train[train.columns[1:]].groupby('ages').corr()['avg_score'].fillna(0).unstack()

corr_reset = corr.reset_index()
sorted_corr = corr_reset.sort_values(by='avg_score', ascending=False)
unique_sorted_corr = sorted_corr.drop_duplicates()
print(unique_sorted_corr.head())


mask = np.zeros_like(corr, dtype=np.bool)
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr.T[2:],  cmap=cmap,  center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.show()

print(corr.head(5))


age_grouped_avg_score = train.groupby('ages')['avg_score'].mean()
sorted_age_grouped_avg_score = age_grouped_avg_score.sort_index()
print(sorted_age_grouped_avg_score)