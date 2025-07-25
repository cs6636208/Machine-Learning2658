import pandas as pd

df = pd.read_csv("sales_data_100.csv")
print(df.head(10))
print()
print(df['Price'].max(), df['Price'].mean())
print()
df['TotalPrice'] = df['Quantity'] * df['Price']
print(df.head(10))
print()
df['Discount'] = [0.10 if category == 'IT' else 0.05 for category in df['Category']]
print(df.head(10))
print()
df['NetPrice'] = df['TotalPrice'] * (1 - df['Discount'])
print(df.head(10))
print()
print(df.groupby('Category')['TotalPrice'].sum())
print()
print(df.groupby('Region')['TotalPrice'].sum())
print()
product_sales = df.groupby('Product')['Quantity'].sum()
top_5_products = product_sales.sort_values(ascending=False).head(5)
print(top_5_products)
print()
top_5_products = product_sales.sort_values(ascending=False).head(5).reset_index
print(top_5_products, "555555")
print()
bottom_5_products = product_sales.sort_values().head(5).reset_index()
# print(top_5_products['Product'])
print(bottom_5_products['Product'])
print()
xxx = df.groupby('Product')['Quantity'].sum().reset_index()
print(xxx.loc[xxx['Quantity'] < 20])