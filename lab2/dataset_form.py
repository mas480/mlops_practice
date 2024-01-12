import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

SKZ_vibration_speed_res = []
scope1_res = []
scope2_res = []
scope3_res = []
scope4_res = []
scope5_res = []
scope6_res = []
scope7_res = []
scope8_res = []
defect_type_res = []

i = 0
while (i < 2000):
    SKZ_vibration_speed = np.random.uniform(4.5,40,1)
    scope1 = np.random.uniform(SKZ_vibration_speed[0] * 0.7,500,1)
    scope2 = np.random.uniform(0,scope1[0] / 3,1)
    scope3 = np.random.uniform(0,scope1[0] / 3,1)
    scope4 = np.random.uniform(0,scope1[0] / 3,1)
    scope5 = np.random.uniform(0,scope1[0] / 3,1)
    scope6 = np.random.uniform(0,scope1[0] / 3,1)
    scope7 = np.random.uniform(0,scope1[0] / 3,1)
    scope8 = np.random.uniform(0,scope1[0] / 3,1)
    
    
    if ((SKZ_vibration_speed[0] >= 4.5) & 
        (scope1[0] >= SKZ_vibration_speed[0] * 0.7) &
        (scope2[0] <= scope1[0] / 3) & 
        (scope3[0] <= scope1[0] / 3) & 
        (scope4[0] <= scope1[0] / 3) &
        (scope5[0] <= scope1[0] / 3) & 
        (scope6[0] <= scope1[0] / 3) & 
        (scope7[0] <= scope1[0] / 3) &
        (scope8[0] <= scope1[0] / 3)):
        i += 1
        
        SKZ_vibration_speed_res.append(SKZ_vibration_speed[0])
        scope1_res.append(scope1[0])
        scope2_res.append(scope2[0])
        scope3_res.append(scope3[0])
        scope4_res.append(scope4[0])
        scope5_res.append(scope5[0])
        scope6_res.append(scope6[0])
        scope7_res.append(scope7[0])
        scope8_res.append(scope8[0])
        defect_type_res.append(1)
        
i = 0
while (i < 2000):
    SKZ_vibration_speed = np.random.uniform(4.5,40,1)
    scope1 = np.random.uniform(0,500,1)
    scope2 = np.random.uniform(0,500,1)
    scope3 = np.random.uniform(0,500,1)
    scope4 = np.random.uniform(0,500,1)
    scope5 = np.random.uniform(0,500,1)
    scope6 = np.random.uniform(0,500,1)
    scope7 = np.random.uniform(0,500,1)
    scope8 = np.random.uniform(0,500,1)
    
    if (((SKZ_vibration_speed[0] >= 4.5) & 
         ((scope1[0] + scope2[0] + scope3[0]) >= SKZ_vibration_speed[0] * 0.8) &
         ((scope1[0] / scope2[0]) >= 0.7) &
         ((scope1[0] / scope2[0]) <= 1.3) &
         ((scope2[0] / scope3[0]) >= 0.7) &
         ((scope2[0] / scope3[0]) <= 1.3) &
         ((scope1[0] / scope3[0]) >= 0.7) & 
         ((scope1[0] / scope3[0]) <= 1.3) &
         (scope4[0] <= (scope1[0] / 3)) & 
         (scope5[0] <= (scope1[0] / 3)) & 
         (scope6[0] <= (scope1[0] / 3)) &
         (scope7[0] <= (scope1[0] / 3)) & 
         (scope8[0] <= (scope1[0] / 3))) |
         (((scope1[0] + scope2[0] + scope3[0] + scope4[0] + scope5[0] + scope6[0] + scope7[0] + scope8[0]) >= (SKZ_vibration_speed[0] * 0.8)) &
         ((scope1[0] / scope2[0]) >= 0.7) & 
         ((scope1[0] / scope2[0]) <= 1.3) &
         ((scope2[0] / scope3[0]) >= 0.7) & 
         ((scope2[0] / scope3[0]) <= 1.3) &
         # ((scope3[0] / scope4[0]) >= 0.7) & 
         # ((scope3[0] / scope4[0]) <= 1.3) &
         # ((scope4[0] / scope5[0]) >= 0.7) & 
         # ((scope4[0] / scope5[0]) <= 1.3) &
         # ((scope5[0] / scope6[0]) >= 0.7) & 
         # ((scope5[0] / scope6[0]) <= 1.3) &
         # ((scope6[0] / scope7[0]) >= 0.7) & 
         # ((scope6[0] / scope7[0]) <= 1.3) &
         # ((scope7[0] / scope8[0]) >= 0.7) & 
         ((scope7[0] / scope8[0]) <= 1.3))):
        i += 1
        
        SKZ_vibration_speed_res.append(SKZ_vibration_speed[0])
        scope1_res.append(scope1[0])
        scope2_res.append(scope2[0])
        scope3_res.append(scope3[0])
        scope4_res.append(scope4[0])
        scope5_res.append(scope5[0])
        scope6_res.append(scope6[0])
        scope7_res.append(scope7[0])
        scope8_res.append(scope8[0])
        defect_type_res.append(2)
        
        
i = 0
while (i < 2000):
    SKZ_vibration_speed = np.random.uniform(4.5,40,1)
    scope2 = np.random.uniform(SKZ_vibration_speed[0] * 0.7,500,1)
    scope1 = np.random.uniform(0,scope2[0] / 3,1)
    
    scope3 = np.random.uniform(0,scope2[0] / 3,1)
    scope4 = np.random.uniform(0,scope2[0] / 3,1)
    scope5 = np.random.uniform(0,scope2[0] / 3,1)
    scope6 = np.random.uniform(0,scope2[0] / 3,1)
    scope7 = np.random.uniform(0,scope2[0] / 3,1)
    scope8 = np.random.uniform(0,scope2[0] / 3,1)
    
    if ((SKZ_vibration_speed[0] >= 4.5) &
         (scope2[0] >= (SKZ_vibration_speed[0] * 0.7)) &
         (scope1[0] <= (scope2[0] / 3)) & 
         (scope3[0] <= (scope2[0] / 3)) &
         (scope4[0] <= (scope2[0] / 3)) &
         (scope5[0] <= (scope2[0] / 3)) & 
         (scope6[0] <= (scope2[0] / 3)) & 
         (scope7[0] <= (scope2[0] / 3)) &
         (scope8[0] <= (scope2[0] / 3))):
        i += 1
        
        SKZ_vibration_speed_res.append(SKZ_vibration_speed[0])
        scope1_res.append(scope1[0])
        scope2_res.append(scope2[0])
        scope3_res.append(scope3[0])
        scope4_res.append(scope4[0])
        scope5_res.append(scope5[0])
        scope6_res.append(scope6[0])
        scope7_res.append(scope7[0])
        scope8_res.append(scope8[0])
        defect_type_res.append(3)
        
i = 0
while (i < 2000):
    SKZ_vibration_speed = np.random.uniform(0.1,40,1)
    scope1 = np.random.uniform(0.1,500,1)
    scope2 = np.random.uniform(0.1,500,1)
    scope3 = np.random.uniform(0.1,500,1)
    scope4 = np.random.uniform(0.1,500,1)
    scope5 = np.random.uniform(0.1,500,1)
    scope6 = np.random.uniform(0.1,500,1)
    scope7 = np.random.uniform(0.1,500,1)
    scope8 = np.random.uniform(0.1,500,1)
    if (SKZ_vibration_speed[0] < 4.5):
        i += 1
        
        SKZ_vibration_speed_res.append(SKZ_vibration_speed[0])
        scope1_res.append(scope1[0])
        scope2_res.append(scope2[0])
        scope3_res.append(scope3[0])
        scope4_res.append(scope4[0])
        scope5_res.append(scope5[0])
        scope6_res.append(scope6[0])
        scope7_res.append(scope7[0])
        scope8_res.append(scope8[0])
        defect_type_res.append(4)
        
        
i = 0
while (i < 2000):
    SKZ_vibration_speed = np.random.uniform(4.5,40,1)
    scope1 = np.random.uniform(0.1,500,1)
    scope2 = np.random.uniform(0.1,500,1)
    scope3 = np.random.uniform(0.1,500,1)
    scope4 = np.random.uniform(0.1,500,1)
    scope5 = np.random.uniform(0.1,500,1)
    scope6 = np.random.uniform(0.1,500,1)
    scope7 = np.random.uniform(0.1,500,1)
    scope8 = np.random.uniform(0.1,500,1)
    
    if ((SKZ_vibration_speed[0] >= 4.5) &
        ~((scope1[0] >= (SKZ_vibration_speed[0] * 0.7)) &
        (scope2[0] <= scope1[0] / 3) & 
        (scope3[0] <= scope1[0] / 3) & 
        (scope4[0] <= scope1[0] / 3) &
        (scope5[0] <= scope1[0] / 3) & 
        (scope6[0] <= scope1[0] / 3) & 
        (scope7[0] <= scope1[0] / 3) &
        (scope8[0] <= scope1[0] / 3)) &
        ~(((scope1 + scope2 + scope3) >= (SKZ_vibration_speed * 0.8)) &
        ((scope1[0] / scope2[0]) >= 0.7) &
        ((scope1[0] / scope2[0]) <= 1.3) &
        ((scope2[0] / scope3[0]) >= 0.7) &
        ((scope2[0] / scope3[0]) <= 1.3) &
        ((scope1[0] / scope3[0]) >= 0.7) &
        ((scope1[0] / scope3[0]) <= 1.3) &
        (scope4[0] <= (scope1[0] / 3)) &
        (scope5[0] <= (scope1[0] / 3)) &
        (scope6[0] <= (scope1[0] / 3)) &
        (scope7[0] <= (scope1[0] / 3)) &
        (scope8[0] <= (scope1[0] / 3))) &
        ~(((scope1[0] + scope2[0] + scope3[0] + scope4[0] + scope5[0] + scope6[0] + scope7[0] + scope8[0]) >= (SKZ_vibration_speed[0] * 0.8)) &
        ((scope1[0] / scope2[0]) >= 0.7) & 
        ((scope1[0] / scope2[0]) <= 1.3) &
        ((scope2[0] / scope3[0]) >= 0.7) & 
        ((scope2[0] / scope3[0]) <= 1.3) &
        ((scope3[0] / scope4[0]) >= 0.7) & 
        ((scope3[0] / scope4[0]) <= 1.3) &
        ((scope4[0] / scope5[0]) >= 0.7) & 
        ((scope4[0] / scope5[0]) <= 1.3) &
        ((scope5[0] / scope6[0]) >= 0.7) & 
        ((scope5[0] / scope6[0]) <= 1.3) &
        ((scope6[0] / scope7[0]) >= 0.7) & 
        ((scope6[0] / scope7[0]) <= 1.3) &
        ((scope7[0] / scope8[0]) >= 0.7) & 
        ((scope7[0] / scope8[0]) <= 1.3)) &
        ~((scope2[0] >= (SKZ_vibration_speed[0] * 0.7)) &
        (scope1[0] <= (scope2[0]) / 3) &
        (scope3[0] <= (scope2[0]) / 3) &
        (scope4[0] <= (scope2[0]) / 3) &
        (scope5[0] <= (scope2[0]) / 3) &
        (scope6[0] <= (scope2[0]) / 3) &
        (scope7[0] <= (scope2[0]) / 3) &
        (scope8[0] <= (scope2[0]) / 3))
       ):

        i += 1
        
        SKZ_vibration_speed_res.append(SKZ_vibration_speed[0])
        scope1_res.append(scope1[0])
        scope2_res.append(scope2[0])
        scope3_res.append(scope3[0])
        scope4_res.append(scope4[0])
        scope5_res.append(scope5[0])
        scope6_res.append(scope6[0])
        scope7_res.append(scope7[0])
        scope8_res.append(scope8[0])
        defect_type_res.append(5)
        
        
state_res = []
for i in range(len(defect_type_res)):
    if (SKZ_vibration_speed_res[i] < 4.5):
        state_res.append(1)
    elif ((SKZ_vibration_speed_res[i] >= 4.5) &
          (SKZ_vibration_speed_res[i] < 7.1) &
          (defect_type_res[i] == 4)):
        state_res.append(2)
    elif (((SKZ_vibration_speed_res[i] >= 4.5) &
          (SKZ_vibration_speed_res[i] < 7.1)) &
          ((defect_type_res[i] == 1) |
          (defect_type_res[i] == 2) |
          (defect_type_res[i] == 3) |
          (defect_type_res[i] == 5))):
        state_res.append(3)
    elif ((SKZ_vibration_speed_res[i] >= 7.1) &
          (SKZ_vibration_speed_res[i] < 11.2)):
        state_res.append(4)
    elif (SKZ_vibration_speed_res[i] >= 11.2):
        state_res.append(5)
        
        
time_to_break_res = []
for i in range(len(state_res)):
    if (state_res[i] == 5):
        time = np.random.randint(1,12,1)
        time_to_break_res.append(time[0])
    elif (state_res[i] == 4):
        time = np.random.randint(12,24,1)
        time_to_break_res.append(time[0])
    elif (state_res[i] == 3):
        time = np.random.randint(24,36,1)
        time_to_break_res.append(time[0])
    elif (state_res[i] == 2):
        time = np.random.randint(36,48,1)
        time_to_break_res.append(time[0])
    elif (state_res[i] == 1):
        time = np.random.randint(48,60,1)
        time_to_break_res.append(time[0])
        
work_hours = np.random.randint(1,172800,10000)
repair_days = np.random.randint(1,720,10000)
repair_period = np.random.randint(1,720,10000)


df_new = pd.DataFrame()
df_new['SKZ_vibration_speed'] = SKZ_vibration_speed_res
df_new['scope1'] = scope1_res
df_new['scope2'] = scope2_res
df_new['scope3'] = scope3_res
df_new['scope4'] = scope4_res
df_new['scope5'] = scope5_res
df_new['scope6'] = scope6_res
df_new['scope7'] = scope7_res
df_new['scope8'] = scope8_res
df_new['repair_days'] = repair_days
df_new['repair_period'] = repair_period
df_new['work_hours'] = work_hours
df_new['defect_type'] = defect_type_res
df_new['state'] = state_res
df_new['time_to_break'] = time_to_break_res

df_new_2 = df_new.sample(frac=1).reset_index(drop=True)


df_train, df_test = train_test_split(df_new_2, test_size=0.2, random_state=42)

df_train.to_csv('data_pred_analytics_train.csv', index=False)
df_test.to_csv('data_pred_analytics_test.csv', index=False)