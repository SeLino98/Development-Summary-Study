


import pandas as pd

df = pd.DataFrame.dropna()
# subset

Q1,Q3 = df['col'].quantile([0.25,0.75])

df['asdf'].str.contains("asdf")
A  =df['date_added'].astype('datetime64[ns]')

A = pd.to_datetime(df['adsf'])

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y,stratify=Y,test_size =0.2, random_state=123)
model = RandomForestClassifier(max_depth=4,random_state=123).fit(x_train,y_train)

final_model = model
pred = final_model.predict(x_submission)

pd.DataFrame({'PRED':pred}).to_csv('result.csv',index=False)

tmp = pd.read_csv('result.csv')

tmp.shape
print(tmp.value_counts(normalize=True))


