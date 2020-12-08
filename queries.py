import datetime as dt
import numpy as np
#import statsmodels.api as sm
#import statsmodels.formula.api as smf

import san
import pandas as pd 
#all_projects = san.get("projects/all")
N=3

from_date = '2017-01-01'
to_date = '2020-12-01'
asset = 'ethereum'
interval = '1d'

# create batch object
batch = san.Batch()

# create a request
batch.get(
    f'daily_active_addresses/{asset}',
    from_date=from_date,
    to_date=to_date,
    interval=interval
)
batch.get(
    f'daily_active_deposits/{asset}',
    from_date=from_date,
    to_date=to_date,
    interval=interval
)
batch.get(
    f'prices/{asset}',
    from_date=from_date,
    to_date=to_date,
    interval=interval
)

# execute the request
[daa, dad, price] = batch.execute()

# merge dataframes
data = daa.rename(columns={'value':'activeAddresses'}).join(dad).join(price['priceUsd'])
data['asset']=asset
# take a look
print(data.head())

#all_projects.to_csv('all_projects.csv', header=True, encoding='utf-8')
#print(all_projects.head())
#pd.DataFrame(all_projects['projectBySlug'], index=[0])
"""
for asset, score in assets_scores:
    if score in sorted(performances)[:N] and score > tolerance: #this is the realized performance! 
        label=1
    elif score in sorted(performances)[-N:] and score < -tolerance: 
        label=-1
    else:
        label=0
"""


