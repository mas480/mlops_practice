import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df_train = pd.read_csv('train/preprocessed_train.csv')

X_train = df_train.iloc[:, :-1].values
y_train = df_train.iloc[:, -1].values

model = LinearRegression(fit_intercept=False)
reg = model.fit(X_train, y_train)

pkl_filename = "reg_model.pkl" 
with open(pkl_filename, 'wb') as file: 
    pickle.dump(model, file) 