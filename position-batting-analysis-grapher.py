import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/wRCplus-data-total.csv")

positions = ['1b', '2b', '3b', 'ss', 'c', 'cf', 'lf', 'rf', 'of']

for pos in positions:
    plot = sns.lineplot(data = df, x = df['season'], y = df[f'wavgwRC+_{pos}'], color = "black") # line plot itself
    z = np.polyfit(df['season'], df[f'wavgwRC+_{pos}'], deg = 1)
    p = np.poly1d(z)
    plt.plot(df['season'], p(df['season']), color = "black", linestyle = ":") # trendline
    plt.xlabel("Season")
    plt.ylabel("Weighted Avg wRC+")
    plt.title(f"Weighted Average wRC+ Over Time ({pos}), 162-game era (1962-2022)")
    axis = plt.gca()
    axis.set_ylim([60, 140])
    plt.axhline(y = 100, color = "grey", linestyle = "dashed", alpha = 0.7) # average
    plt.show()