import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import os

def data_creation(count_data):
    # создание датасета
    max_sp = np.random.normal(180, 40, count_data) + np.random.uniform(0, 10, count_data)
    ac_one = np.random.normal(8, 6, count_data) + np.random.uniform(0, 2, count_data)
    v = np.random.normal(2000, 1000, count_data)
    
    data = {'max_sp': max_sp, 'ac_one': ac_one, 'v': v} 
    df = pd.DataFrame(data) 
    
    # если разгон до 100км/ч меньше 6 секунд - кол-во л/с больше 200
    df['hp'] = df['ac_one'].apply(lambda x: 1 if x < 6 else 0)
    
    df_train, df_test = train_test_split(df, test_size=0.3, random_state=42)
    
    return df_train, df_test

def data_preprocessing(df_train, df_test):
    # принимаем, что разгон до 100 км/ч менее 3 сек - выбросы
    filt_train = ((df_train['ac_one'] > 3))
    filt_test = ((df_test['ac_one'] > 3))
    df_train, df_test = df_train[filt_train], df_test[filt_test]
    
    # Стандартизация
    scaler = StandardScaler()
    df_train.iloc[:, :-1] = scaler.fit_transform(df_train.iloc[:, :-1])
    df_test.iloc[:, :-1] = scaler.fit_transform(df_test.iloc[:, :-1])
    
    return df_train, df_test

def model_reg(count_data):
    df_train_creat, df_test_creat = data_creation(count_data)
    df_train, df_test = data_preprocessing(df_train_creat, df_test_creat)
    X_train = df_train.iloc[:, :-1].values
    y_train = df_train.iloc[:, -1].values
    X_test = df_test.iloc[:, :-1].values
    y_test = df_test.iloc[:, -1].values
    
    model = LinearRegression(fit_intercept=False)
    reg = model.fit(X_train, y_train)
    res = round(model.score(X_test, y_test),3)
    return res