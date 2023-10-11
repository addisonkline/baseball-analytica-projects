import pandas as pd
import numpy as np
import time
from pybaseball import pitching_stats
from sklearn.linear_model import LogisticRegression

pitchers = pd.DataFrame()

for year in range(2006, 2022):
    if (not year == 2020):
        print(f'Current year: {year}')
        time.sleep(2.5)
        this_year = pitching_stats(year)
        pitchers = pd.concat([pitchers, this_year], ignore_index=True)

# add cy young binary
pitchers['cy_young'] = np.zeros(pitchers.shape[0], dtype=np.int16)
cy_young_winners = pd.read_csv('data/cy-young-winners.csv')
for year in range(2006, 2022):
    if (not year == 2020):
        cy_winners = cy_young_winners[cy_young_winners['season'] == year]
        # set value of cy_young to 1 for cy young winners
        pitchers.loc[(pitchers['Season'] == year) & (pitchers['Name'] == cy_winners.iloc[0].get('pitcher')), 'cy_young'] = 1
        pitchers.loc[(pitchers['Season'] == year) & (pitchers['Name'] == cy_winners.iloc[1].get('pitcher')), 'cy_young'] = 1

print(pitchers)

# now perform logistic regression
reduced_df = pd.DataFrame({"W": pitchers['W'], 
                           "WAR": pitchers['WAR'], 
                           "ERA": pitchers['ERA'], 
                           "CG": pitchers['CG'], 
                           "ShO": pitchers['ShO'], 
                           "IP": pitchers['IP'], 
                           "SO": pitchers['SO'], 
                           "K/9": pitchers['K/9'], 
                           "BB/9": pitchers['BB/9'], 
                           "HR/9": pitchers['HR/9'], 
                           "K/BB": pitchers['K/BB'], 
                           "WHIP": pitchers['WHIP']})
model = LogisticRegression(random_state = 0, max_iter = 250).fit(X = reduced_df, y = pitchers['cy_young'])
print(model.score(reduced_df, pitchers['cy_young']))

# now add cy young probabilities to original df
print(model.predict_proba(reduced_df))