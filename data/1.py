import pandas as pd


df = pd.read_csv('model_state.csv')
df['Brand'] = df['Model'].apply(lambda x: x.split()[0])
df['Location'] = df['Location_State'].str.replace('Penang', 'Pulau Pinang')
df.to_csv('brand_data.csv', index=False)

