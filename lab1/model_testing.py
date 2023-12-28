import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

pkl_filename = "reg_model.pkl" 
with open(pkl_filename, 'rb') as file: 
    model = pickle.load(file) 

df_test = pd.read_csv('test/preprocessed_test.csv')
X_test = df_test.iloc[:, :-1].values
y_test = df_test.iloc[:, -1].values

print(f'Model test accuracy is: {round(model.score(X_test, y_test),3)}')