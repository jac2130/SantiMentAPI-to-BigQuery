import datetime as dt
import numpy as np
#import statsmodels.api as sm
#import statsmodels.formula.api as smf
#from utils import get_san_metric
from san.graphql import execute_gql
import san
san.ApiConfig.api_key = 'bajd3fwy257xdmiz_xqbew5vh4u3vrahd'
import pandas as pd 
#all_projects = san.get("projects/all")
N=3

from_date = '2017-06-01'
to_date = '2017-06-04'
#asset = 'bitcoin'
interval = '1d'
assets=['bitcoin', 'ethereum']#, 'bitcoin']
# create batch object
#batch = san.Batch()


all_metrics = {asset: san.available_metrics_for_slug(asset) for asset in assets}

queries = {slug: "{\n "+f"projectBySlug(slug: '{slug}')" + "   {"  for slug in assets}

for query in queries:
    queries[query] += '\n     '+ '\n     '.join([metric for metric in all_metrics[query][:3]]) + "\n }\n}"

for asset in assets:
    res = execute_gql("{\n " + f'projectBySlug(slug: "{asset}")' + " {\n        availableTimeseriesMetrics\n        }\n}")

#ethereum_df =pd.DataFrame(res['projectBySlug'], index=[0])
    all_metrics= res['projectBySlug']['availableTimeseriesMetrics']
    prices = san.get(f'prices/{asset}', from_date=from_date, to_date=to_date, interval=interval)
    data=prices
    for metric in all_metrics:
        
        if san.metadata(metric, arr=['isAccessible', 'isRestricted'])['isRestricted']:
            continue
        else:
            data=data.join(san.get(f'{metric}/{asset}', from_date=from_date, to_date=to_date, interval=interval).rename(columns={'value':metric}))

    print(data.head())
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


