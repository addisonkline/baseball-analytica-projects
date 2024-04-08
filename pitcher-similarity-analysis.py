import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/pitcher_daera_similarity_2022_2023_120ip.csv')
cols = pd.read_csv('data/archive/pitching_stats/pitching_stats_2022.csv')
cols = cols.loc[cols['IP'] >= 120, 'Name'].values
#print(cols)

hist = df.hist(color='grey')
plt.show()

scores = []
for i, row in df.iterrows():
    pitcher = row.get('Name')

    min_score = 2**64
    min_pitcher = ""
    for col in cols:
        this_score = df.loc[i, col]
        scores.append(this_score)
        if this_score < min_score:
            min_score = this_score
            min_pitcher = col
    
    print(f'2023 {pitcher} is most similar to 2022 {min_pitcher} (score = {min_score})')

hist = sns.histplot(x=scores, color='grey')
plt.title('Distribution of All Similarity Scores in Sample (n = 10,608)')
plt.xlabel('Similarity Score')
plt.show()