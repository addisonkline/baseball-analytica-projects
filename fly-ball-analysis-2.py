import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

teams = ['NYY']

for team in teams:
    df = pd.read_csv(f'data/fly_balls_plus_climate_{team}.csv')

    # temp
    hist = sns.histplot(x=df['temp'], binwidth=5)
    plt.show()

    temp_bin1 = df.loc[df['temp'] < 15]
    temp_bin2 = df.loc[(df['temp'] >= 15) & (df['temp'] < 20)]
    temp_bin3 = df.loc[(df['temp'] >= 20) & (df['temp'] < 25)]
    temp_bin4 = df.loc[df['temp'] >= 25]

    temp_bins = ['<15.0', '15.0-19.9', '20.0-24.9', '>=25.0']
    temp_bin_vals = [temp_bin1['hr_count'].sum() / temp_bin1['fb_count'].sum(), temp_bin2['hr_count'].sum() / temp_bin2['fb_count'].sum(), temp_bin3['hr_count'].sum() / temp_bin3['fb_count'].sum(), temp_bin4['hr_count'].sum() / temp_bin4['fb_count'].sum()]

    bp = sns.barplot(x=temp_bins, y=temp_bin_vals, color='grey')
    plt.title('Home Run Rate by Temperature, Yankee Stadium, 2023')
    plt.xlabel('Game Temperature (C)')
    plt.ylabel('HR/FB')
    plt.show()

    # dew point
    hist = sns.histplot(x=df['dewpoint'], binwidth=5)
    plt.show()

    dp_bin1 = df.loc[df['dewpoint'] < 0]
    dp_bin2 = df.loc[(df['dewpoint'] >= 0) & (df['dewpoint'] < 5)]
    dp_bin3 = df.loc[(df['dewpoint'] >= 5) & (df['dewpoint'] < 10)]
    dp_bin4 = df.loc[(df['dewpoint'] >= 10) & (df['dewpoint'] < 15)]
    dp_bin5 = df.loc[(df['dewpoint'] >= 15) & (df['dewpoint'] < 20)]
    dp_bin6 = df.loc[df['dewpoint'] >= 20]

    dp_bins = ['<0.0', '0.0-4.9', '5.0-9.9', '10.0-14.9', '15.0-19.9', '>=20.0']
    dp_bin_vals = [dp_bin1['hr_count'].sum() / dp_bin1['fb_count'].sum(), dp_bin2['hr_count'].sum() / dp_bin2['fb_count'].sum(), dp_bin3['hr_count'].sum() / dp_bin3['fb_count'].sum(), dp_bin4['hr_count'].sum() / dp_bin4['fb_count'].sum(), dp_bin5['hr_count'].sum() / dp_bin5['fb_count'].sum(), dp_bin6['hr_count'].sum() / dp_bin6['fb_count'].sum()]

    bp = sns.barplot(x=dp_bins, y=dp_bin_vals, color='grey')
    plt.title('Home Run Rate by Dew Point, Yankee Stadium, 2023')
    plt.xlabel('Game Dew Point (C)')
    plt.ylabel('HR/FB')
    plt.show()

    sp = sns.scatterplot(x=df['temp'], y=df['hr_rate'], color='black', alpha=0.5)
    plt.show()

    sp = sns.scatterplot(x=df['dewpoint'], y=df['hr_rate'], color='black', alpha=0.5)
    plt.show()

