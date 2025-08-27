import pandas as pd

df = pd.read_csv("sales_data_100.csv")

ans = df.loc[(df['Price'] > 1000) & (df['Category'] == 'Furniture')]
print(ans)

print()

ans = df.loc[(df['OrderDate'] > '2024-02-01') & ((df['Region'] == 'Central') | (df['Region'] == 'North'))]

print()

ans1 = df.groupby(['Region', 'Category'])[['Quantity', 'Price']].sum()
# ans = df.loc[(df['OrderDate'] > '2024-02-01') & (df['Region'].isin(['Central', 'North']))]
print(ans)

print(ans1)