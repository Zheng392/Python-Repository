import json
import pandas as pd
import numpy as np
venues=[]
ids=set()
with open('venues.json','r') as f:
    for line in f.readlines():
        venue=json.loads(line)['venue']
        venues.append([venue['id'],venue['name'],venue['stats']['tipCount'],venue['stats']['usersCount'],
                       venue['stats']['checkinsCount'],venue['location']['lat'],
                       venue['location']['lng']])
        ids.add(venue['id'])

df=pd.DataFrame(np.array(venues),columns=['id','name','tipCount','usersCount','checkinsCount','lat','lng'])
df.to_csv('data.csv')
pass