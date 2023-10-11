import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/schedules_by_year_2004_2023.csv')

df = pd.DataFrame()
for year in range(2004, 2024):
    row = pd.DataFrame()
    row.loc[0, 'Season'] = year
    row.loc[0, 'schedulerank_stdev'] = data.loc[data['Season'] == year, 'schedulerank'].std() # standard deviation
    row.loc[0, 'schedulerank_range'] = data.loc[data['Season'] == year, 'schedulerank'].max() - data.loc[data['Season'] == year, 'schedulerank'].min() # range
    row.loc[0, 'schedulerank_mid50'] = data.loc[data['Season'] == year, 'schedulerank'].sort_values().iloc[22] - data.loc[data['Season'] == year, 'schedulerank'].sort_values().iloc[8]
    row.loc[0, 'oppW%_stdev'] = data.loc[data['Season'] == year, 'oppW%'].std() # standard deviation
    row.loc[0, 'oppW%_range'] = data.loc[data['Season'] == year, 'oppW%'].max() - data.loc[data['Season'] == year, 'oppW%'].min() # range
    row.loc[0, 'oppW%_mid50'] = data.loc[data['Season'] == year, 'oppW%'].sort_values().iloc[22] - data.loc[data['Season'] == year, 'oppW%'].sort_values().iloc[8]

    df = pd.concat([df, row])
    #print(data.loc[data['Season'] == year, 'schedulerank'].std())

print(df)

sns.stripplot(data=data, x='Season', y='oppW%', color='black', alpha=0.5)
plt.xticks(rotation=60)
plt.yticks(np.arange(0.460,0.540,0.010))
plt.title('Plot of Team Opponent Winning Pctg by Season, All MLB Teams (2004-2023)')
plt.ylabel('Team Opponent W%')
plt.xlabel('Season')
plt.show()

sns.stripplot(data=data, x='Season', y='schedulerank', color='black', alpha=0.5)
plt.xticks(rotation=60)
plt.yticks(np.arange(0.460,0.540,0.010))
plt.title('Plot of Team Opponent Skill by Season, All MLB Teams (2004-2023)')
plt.ylabel('Team Opponent Skill')
plt.xlabel('Season')
plt.show()

sns.lineplot(x=np.arange(2004,2024,1).astype(int), y=df['schedulerank_stdev'], color='black')
sns.lineplot(x=np.arange(2004,2024,1).astype(int), y=df['oppW%_stdev'], color='grey', alpha=0.8)
plt.ylim((0, 0.024))
plt.xticks(np.arange(2004,2024,1).astype(int), rotation=60)
plt.title('Standard Deviation of Team Opponent Skill by Season (2004-2023)')
plt.xlabel('Season')
plt.ylabel('Standard Deviation of Opponent Skill/W%')
plt.show()

sns.lineplot(x=np.arange(2004,2024,1).astype(int), y=df['schedulerank_range'], color='black')
sns.lineplot(x=np.arange(2004,2024,1).astype(int), y=df['oppW%_range'], color='grey', alpha=0.8)
plt.ylim((0.025, 0.075))
plt.xticks(np.arange(2004,2024,1).astype(int), rotation=60)
plt.title('Range of Team Opponent Skill by Season (2004-2023)')
plt.xlabel('Season')
plt.ylabel('Range of Opponent Skill/W%')
plt.show()

sns.lineplot(x=np.arange(2004,2024,1).astype(int), y=df['schedulerank_mid50'], color='black')
sns.lineplot(x=np.arange(2004,2024,1).astype(int), y=df['oppW%_mid50'], color='grey', alpha=0.8)
plt.ylim((0, 0.024))
plt.xticks(np.arange(2004,2024,1).astype(int), rotation=60)
plt.title('Middle 50% Range of Team Opponent Skill by Season (2004-2023)')
plt.xlabel('Season')
plt.ylabel('Middle 50% Range of Opponent Skill/W%')
plt.show()