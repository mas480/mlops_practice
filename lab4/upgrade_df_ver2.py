import pandas as pd

df_ver2 = pd.read_csv('./datasets/df_ver1.csv')
df_ver2['Age'] = df_ver2['Age'].fillna(df_ver2.Age.mean())
df_ver2.to_csv('./datasets/df_ver1.csv')
