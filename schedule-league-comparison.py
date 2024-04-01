import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/divisions_by_difficulty_2004_2023.csv')
df_teams = pd.read_csv('data/schedules_by_year_2004_2023_incl_div.csv')

# filter out 2020
df = df.loc[df['Season'] != 2020]
df_teams = df_teams.loc[df_teams['Season'] != 2020] 

# first, isolate league and region from division name
leagues = []
divisions_nolg = []
for i, row in df.iterrows():
    division = row.get('Division')
    leagues.append(division[0:2])
    divisions_nolg.append(division[3:])

df['League'] = leagues
df['Region'] = divisions_nolg

leagues_teams = []
divisions_nolg_teams = []
for i, row in df_teams.iterrows():
    division = row.get('Division')
    leagues_teams.append(division[0:2])
    divisions_nolg_teams.append(division[3:])

df_teams['League'] = leagues_teams
df_teams['Region'] = divisions_nolg_teams

# get a graph of division difficulty by league and region
plot = sns.stripplot(data=df, x='Region', y='oppW%', hue='League', dodge=True, order=['East', 'Central', 'West'], palette='deep')
plt.title('Opponent W% by League and Region, 2004-2023')
plt.ylabel('Opponent W%')
plt.show()

plot = sns.stripplot(data=df, x='Region', y='schedulerank', hue='League', dodge=True, order=['East', 'Central', 'West'], palette='deep')
plt.title('Schedule Rank by League and Region, 2004-2023')
plt.ylabel('Schedule Rank')
plt.show()

# get a violin plot of AL vs NL in general
plot = sns.violinplot(data=df, x='League', y='oppW%', palette='deep')
plt.title('Opponent W% by League, 2004-2023')
plt.ylabel('Opponent W%')
plt.show()
print(f"Mean oppW% AL: {df.loc[df['League'] == 'AL', 'oppW%'].mean()}, sd: {df.loc[df['League'] == 'AL', 'oppW%'].std()}, n: {df.loc[df['League'] == 'AL', 'oppW%'].__len__()}")
print(f"Mean oppW% NL: {df.loc[df['League'] == 'NL', 'oppW%'].mean()}, sd: {df.loc[df['League'] == 'NL', 'oppW%'].std()}, n: {df.loc[df['League'] == 'NL', 'oppW%'].__len__()}")

plot = sns.violinplot(data=df, x='League', y='schedulerank', palette='deep')
plt.title('Schedule Rank by League, 2004-2023')
plt.ylabel('Schedule Rank')
plt.show()
print(f"Mean schedulerank AL: {df.loc[df['League'] == 'AL', 'schedulerank'].mean()}, sd: {df.loc[df['League'] == 'AL', 'schedulerank'].std()}, n: {df.loc[df['League'] == 'AL', 'oppW%'].__len__()}")
print(f"Mean schedulerank NL: {df.loc[df['League'] == 'NL', 'schedulerank'].mean()}, sd: {df.loc[df['League'] == 'NL', 'schedulerank'].std()}, n: {df.loc[df['League'] == 'NL', 'oppW%'].__len__()}")

#print(df)

# get a violin plot of performance by league
plot = sns.violinplot(data=df_teams, x='League', y='W%', palette='deep')
plt.title('W% by League, 2004-2023')
plt.ylabel('W%')
plt.show()
print(f"Mean W% AL: {df_teams.loc[df_teams['League'] == 'AL', 'W%'].mean()}, sd: {df_teams.loc[df_teams['League'] == 'AL', 'W%'].std()}, {df_teams.loc[df_teams['League'] == 'AL', 'W%'].__len__()}")
print(f"Mean W% NL: {df_teams.loc[df_teams['League'] == 'NL', 'W%'].mean()}, sd: {df_teams.loc[df_teams['League'] == 'NL', 'W%'].std()}, {df_teams.loc[df_teams['League'] == 'NL', 'W%'].__len__()}")

# now, do strip plot to get breakdown by region
plot = sns.stripplot(data=df_teams, x='Region', y='W%', hue='League', dodge=True, order=['East', 'Central', 'West'], palette='deep')
plt.title('W% by League and Region, 2004-2023')
plt.show()

plot = sns.violinplot(data=df_teams, x='League', y='RS/G', palette='deep')
plt.title('Runs Scored per Game by League, 2004-2023')
plt.ylabel('RS/G')
plt.show()
print(f"Mean RS/G AL: {df_teams.loc[df_teams['League'] == 'AL', 'RS/G'].mean()}, sd: {df_teams.loc[df_teams['League'] == 'AL', 'RS/G'].std()}, {df_teams.loc[df_teams['League'] == 'AL', 'W%'].__len__()}")
print(f"Mean RS/G NL: {df_teams.loc[df_teams['League'] == 'NL', 'RS/G'].mean()}, sd: {df_teams.loc[df_teams['League'] == 'NL', 'RS/G'].std()}, {df_teams.loc[df_teams['League'] == 'NL', 'W%'].__len__()}")

# now, do strip plot to get breakdown by region
plot = sns.stripplot(data=df_teams, x='Region', y='RS/G', hue='League', dodge=True, order=['East', 'Central', 'West'], palette='deep')
plt.title('RS/G by League and Region, 2004-2023')
plt.show()

plot = sns.violinplot(data=df_teams, x='League', y='RA/G', palette='deep')
plt.title('Runs Allowed per Game by League, 2004-2023')
plt.ylabel('RA/G')
plt.show()
print(f"Mean RA/G AL: {df_teams.loc[df_teams['League'] == 'AL', 'RA/G'].mean()}, sd: {df_teams.loc[df_teams['League'] == 'AL', 'RA/G'].std()}, {df_teams.loc[df_teams['League'] == 'AL', 'W%'].__len__()}")
print(f"Mean RA/G NL: {df_teams.loc[df_teams['League'] == 'NL', 'RA/G'].mean()}, sd: {df_teams.loc[df_teams['League'] == 'NL', 'RA/G'].std()}, {df_teams.loc[df_teams['League'] == 'NL', 'W%'].__len__()}")

# now, do strip plot to get breakdown by region
plot = sns.stripplot(data=df_teams, x='Region', y='RA/G', hue='League', dodge=True, order=['East', 'Central', 'West'], palette='deep')
plt.title('RA/G by League and Region, 2004-2023')
plt.show()