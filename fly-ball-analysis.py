import pandas as pd
import numpy as np

teams = ['NYY', 'ATL', 'COL', 'LAD', 'MIN', 'KCR']

for team in teams:
    df_statcast = pd.read_csv(f'data/fb_data_2023_{team}.csv')
    df_climate = pd.read_csv(f'data/climate_data_{team}.csv')

    df_climate['Mean Temperature (C)'] = (df_climate['Max Temperature (C)'] +  df_climate['Min Temperature (C)']) / 2

    fb_counts = []
    hr_counts = []
    hr_rates = []
    temps = []
    dewpoints = []

    for date in df_statcast['game_date'].unique():
        fb_counts.append(df_statcast.loc[df_statcast['game_date'] == date, 'events'].__len__())
        hr_counts.append(df_statcast.loc[(df_statcast['game_date'] == date) & (df_statcast['events'] == 'home_run'), 'events'].__len__())
        hr_rates.append(df_statcast.loc[(df_statcast['game_date'] == date) & (df_statcast['events'] == 'home_run'), 'events'].__len__() / df_statcast.loc[df_statcast['game_date'] == date, 'events'].__len__())
        temps.append(df_climate.loc[df_climate['Date'] == date, 'Mean Temperature (C)'].values[0])
        dewpoints.append(df_climate.loc[df_climate['Date'] == date, 'Humidity'].values[0])

    df_new = pd.DataFrame({
        "date": df_statcast['game_date'].unique(),
        "fb_count": fb_counts,
        "hr_count": hr_counts,
        "hr_rate": hr_rates,
        "temp": temps,
        "dewpoint": dewpoints
    })

    df_new = df_new.to_csv(f'data/fly_balls_plus_climate_{team}.csv')