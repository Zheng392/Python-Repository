#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import pandas as pd
import numpy as np
venues=[]
ids=set()
venueLine=[]
photos=[]
tips=[]
with open('venues.json','r',encoding="utf8") as f:
    for line in f.readlines():
        venue=json.loads(line)['venue']
        venues.append([venue['id'],venue['stats']['tipCount'],venue['stats']['checkinsCount'],venue['photos']['count']])
        ids.add(venue['id'])

with open('photosData.json','r',encoding="utf8") as f:
    for line in f.readlines():
        photo=json.loads(line)['id']
        photos.append(photo)

with open('tipsData.json','r',encoding="utf8") as f:
    for line in f.readlines():
        tip=json.loads(line)['id']
        tips.append(tip)

photosSeries=pd.Series(photos)
photosScraperCount=photosSeries.value_counts()

tipsSeries=pd.Series(tips)
tipsScraperCount=tipsSeries.value_counts()

df=pd.DataFrame(np.array(venues),columns=['id','tipsCount','checkinsCount','photosCount'])
df=df.set_index('id')
df=pd.merge(df, pd.DataFrame(tipsScraperCount), left_index=True, right_index=True, how='outer')
df=pd.merge(df, pd.DataFrame(photosScraperCount), left_index=True, right_index=True, how='outer')

df.to_csv('Data analysis result.csv')
pass