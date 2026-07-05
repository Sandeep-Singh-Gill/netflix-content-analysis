import pandas as pd
df = pd.read_csv('netflix_titles.csv')

# fill missing values in 'director', 'cast', and 'country' columns with 'Unknown'
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')

#Dropping rows with missing values in 'date_added' column
df.dropna(subset=['date_added','rating','duration'], inplace=True)

# Removing duplicates
df.drop_duplicates(inplace=True)

#Save cleaned data to a new CSV file
df.to_csv('netflix_titles_cleaned.csv', index=False)

print("Cleaning done")
print("New Shape:",df.shape)
print("Missing Values after cleaning:")
print(df.isnull().sum())