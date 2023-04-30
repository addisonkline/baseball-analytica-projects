import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f

months = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']

# read csv
df = pd.read_csv("data/winning-pct-by-month.csv")

# set up new df for anova
df_anova = pd.DataFrame({
    "season": [],
    "month": [],
    "r^2": []
})

seasons = np.unique(df['season'].values) # easier way to get a list of all seasons

# build df_anova
for season in seasons:
    for month in months:
        df_row = [season, month] # individual row in df_anova
        wins_this_season = df.loc[df['season'] == season, 'season-w']
        month_season_corr = wins_this_season.corr(df.loc[df['season'] == season, f'wpct-{month}'])**2
        df_row.append(month_season_corr)
        df_anova.loc[len(df_anova.index)] = df_row

print(df_anova)

# save results as a csv
df_anova.to_csv("data/winning-pct-r2-by-month.csv")

sns.stripplot(x="month", y="r^2", data=df_anova, color="black", alpha=0.3, s=7)
plt.suptitle(f'R^2 of Relationship Between Winning % and Season W')
plt.title('All months within season, 1998-2022, excluding 2020')
plt.xlabel('Month')
plt.ylabel('R^2')
plt.show()

# actually do the anova part
anova_table = pd.DataFrame({
    "Source": [],
    "SumSquares": [],
    "df": [],
    "MeanSquare": [],
    "F": [],
    "p": [] 
})

# adjust R^2 scale because when it's between 0 and 1 the squares make things smaller
#df_anova['r^2'] = 100*df_anova['r^2']

# between groups
mean_total = df_anova['r^2'].mean()
sumsq_between = np.sum((df_anova['r^2'] - mean_total)**2)
df_between = 5 # = k - 1
meansq_between = sumsq_between / df_between
anova_table.loc[len(anova_table.index)] = ["Between Months", sumsq_between, df_between, meansq_between, 0.0, 0.0] # f and p will be filled in later

# within groups
sumsq_within = 0
for month in months: # iterate through each month to add to sumsq_within
    this_month = df_anova.loc[df_anova['month'] == month, 'r^2']
    mean_month = this_month.mean()
    print(f'Mean value for {month}: {mean_month}')
    sumsq_month = np.sum((this_month - mean_month)**2)
    sumsq_within += sumsq_month
df_within = 138 # = n - k
meansq_within = sumsq_within / df_within
anova_table.loc[len(anova_table.index)] = ["Within Months", sumsq_within, df_within, meansq_within, 0.0, 0.0]

# total, as well as F value and p value
anova_table.loc[len(anova_table.index)] = ["Total", anova_table['SumSquares'].sum(), 143, 0, 0, 0]
anova_table.loc[anova_table['Source'] == "Between Months", "F"] = anova_table.iloc[0].get('MeanSquare') / anova_table.iloc[1].get('MeanSquare')
anova_table.loc[anova_table['Source'] == "Between Months", "p"] = 1 - f.cdf(x = anova_table.iloc[0].get('F'), dfn = anova_table.iloc[0].get('df'), dfd = anova_table.iloc[1].get('df'))

# print table
print(anova_table)
print(1 / anova_table.iloc[0].get('p'))