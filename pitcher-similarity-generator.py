import pandas as pd
import numpy as np

df_first = pd.read_csv('data/archive/pitching_stats/pitching_stats_2023.csv')
df_second = pd.read_csv('data/archive/pitching_stats/pitching_stats_2022.csv')

COEFF_K = 7.07
COEFF_BB = 7.05
COEFF_EV = 0.14
COEFF_LAO = 0.13

# first, filter dfs and calculate necessary stats for future calculations
df_first = df_first[df_first['IP'] >= 120]
df_second = df_second[df_second['IP'] >= 120]
df_first['LAO'] = -0.023*(df_first['LA'] - 14.5)**2 + 3.835
df_second['LAO'] = -0.023*(df_second['LA'] - 14.5)**2 + 3.835

# for reach col (pitcher in df_second), calculate similarity scores to every pitcher in df_first (each row)
matrix = pd.DataFrame()
matrix['Name'] = df_first['Name']

for i, pitcher_2 in df_second.iterrows():
    col = []
    print(f'Currently on pitcher {pitcher_2.get("Name")}')
    for j, pitcher_1 in df_first.iterrows():
        score = np.sqrt((7.07*(pitcher_1.get('K%') - pitcher_2.get('K%'))**2) + (7.05*(pitcher_1.get('BB%') - pitcher_2.get('BB%'))**2) + (0.14*((pitcher_1.get('EV') - pitcher_2.get('EV'))**2)) + (0.13*(pitcher_1.get('LAO') - pitcher_2.get('LAO'))**2))
        col.append(score)

    matrix[pitcher_2.get('Name')] = col

print(matrix)
matrix.to_csv('data/pitcher_daera_similarity_2022_2023_120ip.csv')