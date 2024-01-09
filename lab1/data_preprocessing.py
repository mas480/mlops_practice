import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

df_train = pd.read_csv('train/df_train.csv')
df_test = pd.read_csv('test/df_test.csv')

# принимаем, что разгон до 100 км/ч менее 3 сек - выбросы
filt_train = ((df_train['ac_one'] > 3))
filt_test = ((df_test['ac_one'] > 3))
df_train, df_test = df_train[filt_train], df_test[filt_test]

# Стандартизация
scaler = StandardScaler()
df_train.iloc[:, :-1] = scaler.fit_transform(df_train.iloc[:, :-1])
df_test.iloc[:, :-1] = scaler.fit_transform(df_test.iloc[:, :-1])

# Сохранение обработанных данных в файлы
if not os.path.exists('preprocessed_train'):
    os.makedirs('preprocessed_train')
if not os.path.exists('preprocessed_test'):
    os.makedirs('preprocessed_test')

df_train.to_csv('train/preprocessed_train.csv', index=False)
df_test.to_csv('test/preprocessed_test.csv', index=False)
