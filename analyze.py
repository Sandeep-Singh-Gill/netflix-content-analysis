import pandas as pd
df = pd.read_csv('netflix_titles_cleaned.csv')

# 1 Movies vs TV Shows count
print("=== Movies vs TV Shows count ===")
print(df['type'].value_counts())
print(df['type'].value_counts(normalize=True) * 100)

#2 Trend over the years
print("\n=== Trend over the years ===")
trend = df.groupby(['release_year', 'type']).size().unstack(fill_value=0)
print (trend.tail(10))

#Top 10 genres
print("\n=== Top 10 genres ===")
genres = df['listed_in'].str.split(',').explode().str.strip()
print(genres.value_counts().head(10))

# Top 10 Countries
print("\n=== Top 10 Countries ===")
print(df['country'].value_counts().head(10))
