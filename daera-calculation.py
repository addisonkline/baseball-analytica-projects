from pybaseball import pitching_stats
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

df = pd.DataFrame()

years = [2015, 2016, 2017, 2018, 2021] # years to check as year_1

# iterate through each year from list above
for year in years:
    year_1 = pitching_stats(year).sort_values(by = "IDfg")
    year_2 = pitching_stats(year + 1).sort_values(by = "IDfg")
    #print(year_1)

    overlap = np.array(list(set(year_1['IDfg']).intersection(year_2['IDfg']))) # pitchers who were qualified in both year y and year y + 1
    #print(overlap)

    df_toappend = year_1.loc[year_1['IDfg'].isin(overlap)]
    df_toappend.loc[:, 'ERA_y2'] = year_2.loc[year_2['IDfg'].isin(overlap), 'ERA'].values # ERA for the next year
    df_toappend['LAO'] = -0.0023*(year_1['LA'] - 14.5)**2 + 3.835 # launch angle optimality
    df_toappend['Barrels/PA'] = df_toappend['Barrels'] / df_toappend['TBF']
    #print(df_toappend)
    df = pd.concat([df, df_toappend], ignore_index=True)

print(df) # a df containing all qualifying pitcher seasons in the years above

# create a linear model to find the best coefficients of what will be DAERA
#print(np.array([df['K%'], df['BB%'], df['EV'], df['LAO']]).shape)
daera_model = sm.OLS(endog = df['ERA_y2'], exog = sm.add_constant(np.array([df['K%'], df['BB%'], df['EV'], df['LAO']]).transpose()))
print(daera_model.fit().summary())

df_toappend['DAERA'] = -7.07*df_toappend['K%'] + 7.05*df_toappend['BB%'] + 0.14*df_toappend['EV'] + 0.13*df_toappend['LAO'] - 8.18

print("Correlations with a given stat in year y with ERA in year y + 1")
print(f'ERA: r^2 = {df_toappend["ERA"].corr(df_toappend["ERA_y2"]) ** 2}')
print(f'FIP: r^2 = {df_toappend["FIP"].corr(df_toappend["ERA_y2"]) ** 2}')
print(f'xFIP: r^2 = {df_toappend["xFIP"].corr(df_toappend["ERA_y2"]) ** 2}')
print(f'xERA: r^2 = {df_toappend["xERA"].corr(df_toappend["ERA_y2"]) ** 2}')
print(f'SIERA: r^2 = {df_toappend["SIERA"].corr(df_toappend["ERA_y2"]) ** 2}')
print(f'DAERA: r^2 = {df_toappend["DAERA"].corr(df_toappend["ERA_y2"]) ** 2}')