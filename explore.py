import pandas as pd
df = pd.read_csv('netflix_titles.csv')
print("Shape:",df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn info:")
print(df.info())
print("\Missing Values:")
print(df.isnull().sum())