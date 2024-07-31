import pandas as pd #Analysis
import matplotlib.pyplot as plt #Visulization 시각화
# import seaborn as sns #Visulization 시각화 툴
# import numpy as np #Analysis
# import warnings
#
# from lightgbm import LGBMRegressor
# from xgboost import XGBRegressor

# import eli5
# from eli5.sklearn import PermutationImportance
# import shap

plt.rcParams["figure.facecolor"] = 'w'
plt.rcParams["font.family"] = 'NanumBarunGothic'
plt.rcParams['axes.unicode_minus'] = False


# CSV  파일 경로
# C:\Users\Administrator\Desktop\82407_KCB_financial_style_data\credit_card_data
# C:\Users\Administrator\Desktop\82407_KCB_financial_style_data\jeju_financial_life_data
train = pd.read_csv(r"C:\Users\Administrator\Desktop\82407_KCB_financial_style_data\credit_card_data.csv")
print(train.shape)
print(train.head(5))
print(train.info)


