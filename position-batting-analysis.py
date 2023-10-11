from pybaseball import batting_stats
import pandas as pd
import numpy as np

pd.options.display.max_columns = None

df_final = pd.DataFrame({
    "year": [],
    "wavgwRC+": [],
    "medianwRC+": []
})

for year in range(1962, 2023):
    print(f'Current year: {year}')
    df = batting_stats(year, qual=1, position="SS")
    total_pa = df['PA'].sum()
    weighted_vals = (df['PA'] / total_pa) * df['wRC+'] # wRC+ for each player weighted by the percentage of total PAs they had
    df_final.loc[year - 1962, "year"] = year
    df_final.loc[year - 1962, "wavgwRC+"] = np.sum(weighted_vals)
    df_final.loc[year - 1962, "medianwRC+"] = df['wRC+'].median()

pd.options.display.max_rows = None

print(df_final)
df_final.to_csv("data/wRCplus-data-ss.csv")