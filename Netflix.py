import pandas as pd
import matplotlib.pyplot as plt
netflix = pd.read_csv('netflix_titles.csv')

netflix_sub = netflix[netflix['type'] == 'Movie']

sub = netflix_sub[netflix_sub['release_year'] >= 2000]
sub1 = sub[sub['release_year'] <= 2020]

plt.hist(sub1['release_year'], bins = 10)
plt.title("Distribution of Movie Release Years (2000-2020)")
plt.xlabel("Release Year")
plt.ylabel("number of movies")
plt.show()
