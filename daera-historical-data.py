from pybaseball import pitching_stats, team_pitching
import numpy as np
import pandas as pd
from datetime import date

currentYear = date.today().year

df = pd.DataFrame()

# iterate through all years until now
for year in range(2015, currentYear + 1):
    df_thisyear = pitching_stats(year, qual = 1) # get all pitchers from current year with at least 1 plate appearance allowed
    lg_data = team_pitching(currentYear)
    df_thisyear = df_thisyear[df_thisyear['Events'] > 0] # filter out all pitchers without any batted ball events (shouldn't be many but just to be safe)

    lgERA = 9 * (lg_data['ER'].sum() / lg_data['IP'].sum())
    lgLAO = -0.0023*(lg_data['LA'].mean() - 14.5)**2 + 3.835 # best way to estimate lg avg LAO with what we have
    lgDAERA = -7.07*(lg_data['SO'].sum() / lg_data['TBF'].sum()) + 7.05*(lg_data['BB'].sum() / lg_data['TBF'].sum()) + 0.14*(lg_data['EV'].median()) + 0.13*(lgLAO) - 8.18
    lgDAERAconst = lgERA - lgDAERA # add this to every player's DAERA

    df_toappend = pd.DataFrame() # what is appended to df
    df_toappend[['Season', 'Name', 'Team', 'IP', 'ERA', 'K%', 'BB%', 'EV']] = df_thisyear[['Season', 'Name', 'Team', 'IP', 'ERA', 'K%', 'BB%', 'EV']]
    df_toappend['LAO'] = -0.0023*(df_thisyear['LA'] - 14.5)**2 + 3.835
    df_toappend['DAERA'] = (-7.07*(df_toappend['K%']) + 7.05*(df_toappend['BB%']) + 0.14*(df_toappend['EV']) + 0.13*(df_toappend['LAO']) - 8.18 + lgDAERAconst).round(2)

    # concat this year's DAERA data to overall df
    df = pd.concat([df, df_toappend], ignore_index = True)

print(df)
df.to_csv(f'data/daera-data-2015-{currentYear - 1}.csv')