import datetime as dt
import numpy as np
#import statsmodels.api as sm
#import statsmodels.formula.api as smf
#from utils import get_san_metric
import san
import pandas as pd 
#all_projects = san.get("projects/all")
N=3

from_date = '2017-01-01'
to_date = '2020-12-01'
#asset = 'bitcoin'
interval = '1d'
assets=['bitcoin', 'ethereum']#, 'bitcoin']
# create batch object
#batch = san.Batch()

asset_dict={}
# create a request

for asset in assets:
    all_metrics=san.available_metrics_for_slug(asset)
    batch = san.Batch()
    for metric in sorted(all_metrics)[:int(len(all_metrics)/2)]:

    #batch=san.Batch()
        batch.get(
            f'{metric}/{asset}',
            from_date=from_date,
            to_date=to_date,
            interval=interval
        )
    

    #ex_flow = get_san_metric(from_date, to_date, 'exchange_funds_flow', asset, interval='1d', iterate_over_days=700)
 
    [daa, dad, price, others] = batch.execute()
    daa['asset']=asset
    asset_dict[asset] = daa.rename(columns={'value':'activeAddresses', 'asset':'asset'}).join(dad).join(price[['priceUsd', 'priceBtc', 'volume']]).join(others) #.fillna(0)
    #price['asset'] =asset
    print(asset, asset_dict[asset].head())

# merge dataframes
#data = daa.rename(columns={'value':'activeAddresses'}).join(dad).join(price['priceUsd'])
#data['asset']=asset
# take a look
#print(data.head())
#print(data.describe())
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


