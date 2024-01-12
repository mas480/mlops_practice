import numpy as np
import pandas as pd
import dill
import pickle

from catboost import Pool
from catboost import CatBoostClassifier

df = pd.read_csv('data_pred_analytics_train.csv')
X_train = df.drop(['defect_type', 'state', 'time_to_break'], axis=1)
y_train = df['defect_type']


features_names = list(df.drop(['defect_type', 'state', 'time_to_break'], axis=1).columns)

train_data = Pool(
    data=X_train, 
    label=y_train,
    feature_names=features_names
)


model = CatBoostClassifier(iterations = 1000,
                           early_stopping_rounds=100,
                           verbose = 100,
                           depth = 3)

model.fit(X=train_data)

pickle.dump(model, open('model_defect_type.pkl', 'wb'))