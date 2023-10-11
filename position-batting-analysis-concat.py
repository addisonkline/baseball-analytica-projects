import pandas as pd
import numpy as np

positions = ['1b', '2b', '3b', 'ss', 'c', 'cf', 'lf', 'rf', 'of']

df = pd.DataFrame()
df['season'] = np.arange(1962, 2023, 1, dtype=int)

for pos in positions:
    this_df = pd.read_csv(f'data/wRCplus-data-{pos}.csv')
    df[f'wavgwRC+_{pos}'] = this_df['wavgwRC+']
    df[f'medianwRC+_{pos}'] = this_df['medianwRC+']

print(df)
df.to_csv("data/wRCplus-data-total.csv")