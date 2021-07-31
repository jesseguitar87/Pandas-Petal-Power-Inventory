import pandas as pd

df = inventory = pd.read_csv('inventory.csv')
print(df.head(10))
staten_island = (df.head(10))
product_request = df.product_description

seed_request = df[(df.product_type == 'seeds') & (df.location == 'Brooklyn')]
df['in_stock'] = inventory.quantity.apply(lambda x: 'True' if x > 0 else 'False')

df['total_value'] = df['price'] * df['quantity']

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
df['full_description'] = combine_lambda						  
print(df)
