import pandas as pd


# df = pd.read_csv('model_state.csv')
# df['Brand'] = df['Model'].apply(lambda x: x.split()[0])
# df['Location'] = df['Location_State'].str.replace('Penang', 'Pulau Pinang')
# df.to_csv('brand_data.csv', index=False)

df1 = pd.read_csv('brand_data.csv')
brand = df1['Brand'].value_counts().reset_index()
#rename
brand.columns = ['Brand', 'Count']
print(brand)
#save to csv 
brand.to_csv('brand_count.csv', index=False)
