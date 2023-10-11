from pybaseball import schedule_and_record, team_batting
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

teams = team_batting(2023)['Team'].values
runs = np.array([])
"""
for team in teams:
    time.sleep(2)
    print(f'Currently on team: {team}')
    schedule = schedule_and_record(2023, team)
    runs = np.append(arr=runs, values=schedule['R'])
"""
schedule = schedule_and_record(2023, 'LAD')
print(np.mean(schedule['R']))
plt.hist(schedule['R'])
plt.show()
