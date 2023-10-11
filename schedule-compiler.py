from pybaseball import schedule_and_record, team_pitching
import pandas as pd
import numpy as np
import time

for year in range(2021, 2022):
    print(f'Current year: {year}')

    # compile list of teams
    teams = team_pitching(year).sort_values(by="Team")['Team'].values
    #print(teams)

    # create schedule matchup matrix
    matrix = pd.DataFrame()

    # go through each team's schedule

    for team in teams:
        time.sleep(5)
        sched = schedule_and_record(year, team)
        value_counts = sched['Opp'].value_counts()
        for t in teams: # if team doesn't appear in value_counts, add it with value 0
            if not t in value_counts:
                value_counts[t] = 0
        matrix[team] = value_counts

    matrix = matrix.sort_index() # makes rows alphabetical by team
    matrix = matrix / 162 # to make it proportional--dividing everything by 162 just makes everything easier
    matrix.to_csv(f'data/schedule_matrix_{year}.csv')
    print(f'Schedule matrix for {year} done')
    print(matrix)
    #print(sched)
"""
sched = schedule_and_record(2022, 'NYY')
value_counts = sched['Opp'].value_counts()
for team in teams:
    if not team in value_counts:
        value_counts[team] = 0

print(value_counts)
"""