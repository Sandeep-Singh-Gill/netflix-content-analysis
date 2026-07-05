import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('netflix_titles_cleaned.csv')

# Chart 1 : Movies vs TV Shows count
plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Movies vs TV Shows count')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Chart1movies_vs_tvshows.png')
plt.show()

# 2 Chart 2 : Trend over the years
plt.figure(figsize=(10,5))
trend = df.groupby(['release_year', 'type']).size().unstack()
trend[trend.index >= 2012].plot(color=['skyblue', 'salmon'])
plt.title('Trend over the years')
plt.xlabel('Year')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Chart2trend_over_years.png')
plt.show()  

# 3 Chart 3 : Top 10 genres
plt.figure(figsize=(10,5))
genres = df['listed_in'].str.split(', ').explode().str.strip()
genres.value_counts().head(10).plot(kind='barh', color='lightgreen')
plt.title('Top 10 genres')
plt.xlabel('Count')
plt.tight_layout()
plt.savefig('Chart3_genres.png')
plt.show()

#chart 4 : Top 10 Countries
plt.figure(figsize=(10,5))
df['country'].value_counts().head(10).plot(kind='barh', color='lightcoral')
plt.title('Top 10 Countries')
plt.xlabel('Count')
plt.tight_layout()
plt.savefig('Chart4_countries.png')
plt.show()

print("All Charts saved!")