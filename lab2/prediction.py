import numpy as np
import pandas as pd
import dill
import pickle

model = pickle.load(open('model_defect_type.pkl', 'rb'))
    
df = pd.read_csv('data_pred_analytics_test.csv')
X_test = df.drop(['defect_type', 'state', 'time_to_break'], axis=1)
y_test = df['defect_type']

y_predict2=model.predict(X_test[0:1])
    
if y_predict2 == 1:
    answer = "1. дисбалансы роторов"
elif y_predict2 == 2:
    answer = "2. ослабление крепления опорных узлов"
elif y_predict2 == 3:
    answer = "3. недостаточный натяг подшипника"
elif y_predict2 == 4:
    answer = "4. нет дефекта"
else:
    answer = "5. нетипичная пиковая активаность в целевой полосе пропускания"
    
print(answer)