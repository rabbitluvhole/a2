import pandas as pd


# df = pd.read_csv('model_state.csv')
# df['Brand'] = df['Model'].apply(lambda x: x.split()[0])
# df['Location'] = df['Location_State'].str.replace('Penang', 'Pulau Pinang')
# df.to_csv('brand_data.csv', index=False)

# df1 = pd.read_csv('brand_data.csv')
# brand = df1['Brand'].value_counts().reset_index()
# #rename
# brand.columns = ['Brand', 'Count']
# print(brand)
# #save to csv 
# brand.to_csv('brand_count.csv', index=False)

df2 = pd.read_csv('brand_data.csv')
# extract brand and location
df2 = df2[['Brand', 'Location']]
# group by brand and location
df2 = df2.groupby(['Brand', 'Location']).size().reset_index(name='Count')
print(df2)
#save to csv
df2.to_csv('brand_location.csv', index=False)
