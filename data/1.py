



# # Load data from CSV
# df = pd.read_csv('resale_car_cleaned.csv')

# # Extract Brand from Model
# df['Brand'] = df['Model'].apply(lambda x: x.split()[0])

# # Create a new DataFrame with Brand and List_Price columns
# brand_price_df = df[['Brand', 'List_Price']]

# # Save the new DataFrame to a CSV file
# brand_price_df.to_csv('brand_price.csv', index=False)







import pandas as pd

# Load data from CSV
df = pd.read_csv('listingprice.csv')

# Check min and max listing prices
min_prices = df.groupby('Brand')['List_Price'].min()
max_prices = df.groupby('Brand')['List_Price'].max()

# Display the results
print(pd.DataFrame({'Min Listing Price': min_prices, 'Max Listing Price': max_prices}))






# df1 = pd.read_csv('brand_data.csv')
# brand = df1['Brand'].value_counts().reset_index()
# #rename
# brand.columns = ['Brand', 'Count']
# print(brand)
# #save to csv 
# brand.to_csv('brand_count.csv', index=False)

# df2 = pd.read_csv('brand_data.csv')
# # extract brand and location
# df2 = df2[['Brand', 'Location']]
# # group by brand and location
# df2 = df2.groupby(['Brand', 'Location']).size().reset_index(name='Count')
# print(df2)
# #save to csv
# df2.to_csv('brand_location.csv', index=False)


