import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.min_rows', 20)

data = pd.read_csv('data/schedules_by_year_2004_2023.csv')

# plot regression of team W% and schedule strength
ax = sns.regplot(x='oppW%', y='W%', data=data, order=1, color="black", scatter_kws={'alpha':0.3, 'linewidth':0})
plt.suptitle('Win % vs. Average Opponent Win % by Team, 2004-2023')
plt.xlabel('Opponent Win %')
plt.ylabel('Win %')
plt.title(f"n = {data.shape[0]}, R^2 = {np.round(data['oppW%'].corr(data['W%']) ** 2, 4)}", fontsize = 10, color='grey')
plt.show()

# plot regression of team W% and schedule strength
ax = sns.regplot(x='schedulerank', y='W%', data=data, order=1, color="black", scatter_kws={'alpha':0.3, 'linewidth':0})
plt.suptitle('Win % vs. Schedule Rank by Team, 2004-2023')
plt.xlabel('Schedule Rank')
plt.ylabel('Win %')
plt.title(f"n = {data.shape[0]}, R^2 = {np.round(data['schedulerank'].corr(data['W%']) ** 2, 4)}", fontsize = 10, color='grey')
plt.show()

# rank all teams in dataset by schedule strength metrics
print('1. MLB Teams by Average Opponent Winning Percentage (2004 through 2023)')
print(data.sort_values(by='oppW%', ascending=False))

print('2. MLB Teams by Schedule Rank (2004 through 2023)')
print(data.sort_values(by='schedulerank', ascending=False))

# rank all divisions in dataset by schedule strength metrics
# first, determine the division for each team
division_col = []
for i, row in data.iterrows():
    name = row.get('Team')
    season = row.get('Season')
    
    # determine division val for each team
    if (name == "BAL") or (name == "BOS") or (name == "NYY") or (name == "TBR") or (name == "TOR") or (name == "TBD"):
        division_col.append("AL East")
    elif (name == "CHW") or (name == "CLE") or (name == "DET") or (name == "KCR") or (name == "MIN"):
        division_col.append("AL Central")
    elif (name == "HOU" and season > 2012) or (name == "LAA") or (name == "OAK") or (name == "SEA") or (name == "TEX") or (name == "ANA"):
        division_col.append("AL West")
    elif (name == "ATL") or (name == "MIA") or (name == "NYM") or (name == "PHI") or (name == "WSN") or (name == "FLA") or (name == "MON"):
        division_col.append("NL East")
    elif (name == "CHC") or (name == "CIN") or (name == "MIL") or (name == "PIT") or (name == "STL") or (name == "HOU" and season <= 2012):
        division_col.append("NL Central")
    elif (name == "ARI") or (name == "COL") or (name == "LAD") or (name == "SDP") or (name == "SFG"):
        division_col.append("NL West")
    else:
        print(f"caught team name {name}")

data['Division'] = division_col
print(data)

data.to_csv("data/schedules_by_year_2004_2023_incl_div.csv")

# now create a df of all individual divisions by average oppW% and average schedulerank
divisions = ['AL East', 'AL Central', 'AL West', 'NL East', 'NL Central', 'NL West']

divisions_df = pd.DataFrame({
    "Season": [],
    "Division": [],
    "oppW%": [],
    "schedulerank": []
})
for year in range(2004, 2024):
    for division in divisions:
        section = data.loc[(data['Season'] == year) & (data['Division'] == division)]
        oppW_avg = section['oppW%'].mean()
        schedulerank_avg = section['schedulerank'].mean()
        divisions_df.loc[-1] = [year, division, oppW_avg, schedulerank_avg]
        divisions_df.index = divisions_df.index + 1
        divisions_df = divisions_df.sort_index()

divisions_df.to_csv('data/divisions_by_difficulty_2004_2023.csv')

# finally, we can rank all divisions by schedule strength metrics
print('1. MLB Divisions by Average Opponent Winning Percentage (2004 through 2023)')
print(divisions_df.sort_values(by='oppW%', ascending=False))

print('2. MLB Divisions by Schedule Rank (2004 through 2023)')
print(divisions_df.sort_values(by='schedulerank', ascending=False))