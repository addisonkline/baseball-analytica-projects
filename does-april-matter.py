import pandas as pd
import numpy as np
import time
from pybaseball import schedule_and_record, team_pitching

months = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']

# grand dataframe to contain all info on year-team winning pct and winning pct by month
df = pd.DataFrame({
    "season": [],
    "team": [],
    "season-w": [],
    "wpct-Apr": [],
    "wpct-May": [],
    "wpct-Jun": [],
    "wpct-Jul": [],
    "wpct-Aug": [],
    "wpct-Sep": [],
})

# iterate through all full years 1998-2022
for year in range(1998, 2023):
    # don't include 2020
    print(f'Current season = {year}')
    if (not (year == 2020)):
        # gets list of teams in any given year
        team_pitching_stats = team_pitching(year)
        teams = team_pitching_stats['Team'].values

        for team in teams:
            time.sleep(3.5) # had to put this because I began getting rate limited lmao
            team_season = schedule_and_record(year, team)
            team_season_row = [year, team, team_pitching_stats.loc[team_pitching_stats['Team'] == team, 'W'].values[0]] # append these to the df
            #print(team_season_row)
            team_season[['Weekday', 'Month', 'Day']] = team_season['Date'].str.split(expand=True, n=2) # isolate month from game date
            team_season['W/Lnew'] = team_season['W/L'].str.split(expand=True, pat='-')[0] # otherwise W-wo and L-wo would not be counted

            for month in months:
                counts = team_season.loc[team_season['Month'] == month, 'W/Lnew'].value_counts()
                wpct = counts['W'] / (counts['W'] + counts['L'])
                team_season_row.append(wpct) # append winning pctg for the given month to team_season_row

            df.loc[len(df.index)] = team_season_row

print(df)
# now get R^2 for all month wpcts vs. season wins
for month in months:
    print(f'R^2 for {month}: {(df["season-w"].corr(df[f"wpct-{month}"]))**2}')

# save results as a csv
df.to_csv("data/winning-pct-by-month.csv")

"""
df = schedule_and_record(2022, 'TBR')
df[['Weekday', 'Month', 'Day']] = df['Date'].str.split(expand=True, n=2)
print(df)
"""