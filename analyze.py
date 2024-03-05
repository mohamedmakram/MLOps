import pandas as pd

df = pd.read_csv('data.csv')
print('Preview DataFrame')
# print firt 5 rows
print(df.head())

# statistics about the first row
print("Describe first feature")
print(df['1'].describe())