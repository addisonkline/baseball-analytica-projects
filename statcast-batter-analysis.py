from pybaseball import batting_stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_columns = None

df = pd.DataFrame()
df_total = pd.DataFrame()

for year in range(2015, 2023):
    df_year = batting_stats(year) # get batting stats for year
    df_total = pd.concat([df_total, df_year]) # concatenate unabridged batting stats to df_total
    df_year = df_year[df_year['AVG'] >= 0.300] # filter out all hitters who averaged below .300
    df = pd.concat([df, df_year]) # add abridged df_year to df

print(df)

# HardHit%, Barrel%, EV, K%, Contact%, O-Swing%, Z-Swing%, SwStr%
df_total = pd.DataFrame({
    "Player": df_total['Name'],
    "Season": df_total['Season'],
    "PA": df_total['PA'],
    "AB": df_total['AB'],
    "AVG": df_total['AVG'],
    "HardHit%": df_total['HardHit%'],
    "Barrel%": df_total['Barrel%'],
    "EV": df_total['EV'],
    "K%": df_total['K%'],
    "Contact%": df_total['Contact%'],
    "O-Swing%": df_total['O-Swing%'],
    "Z-Swing%": df_total['Z-Swing%'],
    "SwStr%": df_total['SwStr%']
})

print(df_total)
df_total.to_csv(f'data/batting-average-and-peripherals.csv')

# correlation between HardHit% and AVG
ax = sns.regplot(x = 'HardHit%', y = 'AVG', data = df_total, order=1, color="black", scatter_kws={'alpha':0.3, 'linewidth':0})
plt.xlabel('HardHit%')
plt.ylabel('Average')
plt.suptitle('Batting Average vs. Hard Hit Pctg, qualified hitters, 2015-2022')
plt.title(f"n = {df_total.shape[0]}, R^2 = {np.round(df_total['HardHit%'].corr(df_total['AVG']) ** 2, 4)}", fontsize = 10, color='grey')
plt.show()

ax = sns.regplot(x = 'Barrel%', y = 'AVG', data = df_total, order=1, color="black", scatter_kws={'alpha':0.3, 'linewidth':0})
plt.xlabel('Barrel%')
plt.ylabel('Average')
plt.suptitle('Batting Average vs. Barrel Pctg, qualified hitters, 2015-2022')
plt.title(f"n = {df_total.shape[0]}, R^2 = {np.round(df_total['Barrel%'].corr(df_total['AVG']) ** 2, 4)}", fontsize = 10, color='grey')
plt.show()

ax = sns.regplot(x = 'EV', y = 'AVG', data = df_total, order=1, color="black", scatter_kws={'alpha':0.3, 'linewidth':0})
plt.xlabel('EV')
plt.ylabel('Average')
plt.suptitle('Batting Average vs. Avg Exit Velocity, qualified hitters, 2015-2022')
plt.title(f"n = {df_total.shape[0]}, R^2 = {np.round(df_total['EV'].corr(df_total['AVG']) ** 2, 4)}", fontsize = 10, color='grey')
plt.show()

ax = sns.regplot(x = 'K%', y = 'AVG', data = df_total, order=1, color="black", scatter_kws={'alpha':0.3, 'linewidth':0})
plt.xlabel('K%')
plt.ylabel('Average')
plt.suptitle('Batting Average vs. Strikeout Pctg, qualified hitters, 2015-2022')
plt.title(f"n = {df_total.shape[0]}, R^2 = {np.round(df_total['K%'].corr(df_total['AVG']) ** 2, 4)}", fontsize = 10, color='grey')
plt.show()

ax = sns.regplot(x = 'Contact%', y = 'AVG', data = df_total, order=1, color="black", scatter_kws={'alpha':0.3, 'linewidth':0})
plt.xlabel('Contact%')
plt.ylabel('Average')
plt.suptitle('Batting Average vs. Contact Pctg, qualified hitters, 2015-2022')
plt.title(f"n = {df_total.shape[0]}, R^2 = {np.round(df_total['Contact%'].corr(df_total['AVG']) ** 2, 4)}", fontsize = 10, color='grey')
plt.show()

ax = sns.regplot(x = 'O-Swing%', y = 'AVG', data = df_total, order=1, color="black", scatter_kws={'alpha':0.3, 'linewidth':0})
plt.xlabel('O-Swing%')
plt.ylabel('Average')
plt.suptitle('Batting Average vs. Outside-Zone Swing Pctg, qualified hitters, 2015-2022')
plt.title(f"n = {df_total.shape[0]}, R^2 = {np.round(df_total['O-Swing%'].corr(df_total['AVG']) ** 2, 4)}", fontsize = 10, color='grey')
plt.show()

ax = sns.regplot(x = 'Z-Swing%', y = 'AVG', data = df_total, order=1, color="black", scatter_kws={'alpha':0.3, 'linewidth':0})
plt.xlabel('Z-Swing%')
plt.ylabel('Average')
plt.suptitle('Batting Average vs. Zone Swing Pctg, qualified hitters, 2015-2022')
plt.title(f"n = {df_total.shape[0]}, R^2 = {np.round(df_total['Z-Swing%'].corr(df_total['AVG']) ** 2, 4)}", fontsize = 10, color='grey')
plt.show()

ax = sns.regplot(x = 'SwStr%', y = 'AVG', data = df_total, order=1, color="black", scatter_kws={'alpha':0.3, 'linewidth':0})
plt.xlabel('SwStr%')
plt.ylabel('Average')
plt.suptitle('Batting Average vs. Swinging Strike Pctg, qualified hitters, 2015-2022')
plt.title(f"n = {df_total.shape[0]}, R^2 = {np.round(df_total['SwStr%'].corr(df_total['AVG']) ** 2, 4)}", fontsize = 10, color='grey')
plt.show()

# HardHit%, Barrel%, EV, K%, Contact%, O-Swing%, Z-Swing%, SwStr%