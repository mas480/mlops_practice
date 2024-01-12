import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df_ver2 = pd.read_csv('./datasets/df_ver1.csv')
encoder = OneHotEncoder()
encoder_df = pd.DataFrame(encoder.fit_transform(df_ver2[['Sex']]).toarray(), columns = ['female', 'male'])
df_ver3 = pd.concat([df_ver2, encoder_df], axis=1)
df_ver3.to_csv('./datasets/df_ver1.csv')
