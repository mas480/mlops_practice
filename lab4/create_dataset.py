from catboost.datasets import titanic
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

train, test = titanic()
df = train[['Pclass', 'Sex', 'Age']]

df.to_csv('./datasets/df_ver1.csv', index=False)
