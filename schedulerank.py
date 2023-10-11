from pybaseball import team_batting, team_pitching
import pandas as pd
import numpy as np
import time

df = pd.DataFrame()
for year in range(2004, 2024):
    time.sleep(3)
    print(f'Current season: {year}')
    schedule_matrix = pd.read_csv(f'data/schedule_matrix_{year}.csv')

    team_skill_df = pd.DataFrame()
    pitching_data = team_pitching(year).sort_values(by="Team")
    batting_data = team_batting(year).sort_values(by="Team")
    team_skill_df['Season'] = year*np.ones(30).astype(int)
    team_skill_df['Team'] = pitching_data['Team'].values
    team_skill_df['W%'] = pitching_data['W'].values / (pitching_data['W'].values + pitching_data['L'].values)
    team_skill_df['RS/G'] = batting_data['R'].values / 162
    team_skill_df['RA/G'] = pitching_data['R'].values / 162
    team_skill_df['skill'] = team_skill_df['RS/G']**1.83 / (team_skill_df['RS/G']**1.83 + team_skill_df['RA/G']**1.83)
    team_skill_df['oppW%'] = np.matmul(np.array(schedule_matrix)[:, 1:], team_skill_df['W%'])
    team_skill_df['schedulerank'] = np.matmul(np.array(schedule_matrix)[:, 1:], team_skill_df['skill'])

    #print(team_skill_df)
    # concat this year's df to overall df
    df = pd.concat([df, team_skill_df])

print(df)
df.to_csv('data/schedules_by_year_2004_2023.csv')

"""
    updated_skill = team_skill_df['skill']
    final_skill = pd.Series(np.zeros(30))
    #print(schedule_matrix.shape[1])
    
    for iter in range(8):
        print(f'Current iteration: {iter}')
        updated_skill = np.matmul(np.array(schedule_matrix)[:, 1:], updated_skill)
        final_skill += (1/(2**(iter + 1)))*updated_skill
        #print(final_skill)

    print(final_skill.sum())

    team_skill_df['schedulerank_2'] = final_skill
    print(team_skill_df.sort_values(by="schedulerank_2"))
"""