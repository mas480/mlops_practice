import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os

# создание датасета
max_sp = np.random.normal(180, 40, 5000) + np.random.uniform(0, 10, 5000)
ac_one = np.random.normal(8, 6, 5000) + np.random.uniform(0, 2, 5000)
v = np.random.normal(2000, 1000, 5000)

data = {'max_sp': max_sp, 'ac_one': ac_one, 'v': v} 
df = pd.DataFrame(data) 

# если разгон до 100км/ч меньше 6 секунд - кол-во л/с больше 200
df['hp'] = df['ac_one'].apply(lambda x: 1 if x < 6 else 0)

df_train, df_test = train_test_split(df, test_size=0.3, random_state=42)

# Создание train и test
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('test'):
    os.makedirs('test')
    

df_train.to_csv('train/df_train.csv', index=False)
df_test.to_csv('test/df_test.csv', index=False)

print('ok')