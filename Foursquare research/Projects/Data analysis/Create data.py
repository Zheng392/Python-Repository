import pandas as pd
import random
data=pd.read_csv('photo,user,venue,time.txt',names=("photo","user","venue","time"),encoding='utf-8')
data=data.sort_values('time')
# data['venue']=pd.factorize(data['venue'])[0]
# data['user']=pd.factorize(data['user'])[0]
venueNum=len(pd.factorize(data['venue'])[1])
train=data.iloc[0:110000]
test=data.iloc[110000:]



print('start now')

dropList=[]
for x in range(len(test)):
    if (test.iloc[x]['user'] not in list(train['user'].values) or test.iloc[x]['venue'] not in list(train['venue'].values)):
        dropList.append(x)
test = test.drop(test.index[dropList])


train['venue'],venueIndex=pd.factorize(train['venue'])
train['user'],userIndex=pd.factorize(train['user'])

temp=[]
for venue in test['venue']:
    temp.append(venueIndex.get_loc(venue))
test['venue']=temp

temp=[]
for user in test['user']:
    temp.append(userIndex.get_loc(user))
test['user']=temp



with open('train.tsv','w') as f:
    for x in range(len(train)):
        f.write(str(train.iloc[x]['user'])+'\t'+str(train.iloc[x]['venue'])+'\t'+'1'
        +'\t'+str(train.iloc[x]['time'])+'\t'+str(train.iloc[x]['photo'])+'\n')

print('sucessfully save train.tsv')
with open('test.tsv','w') as f:
    for x in range(len(test)):
        f.write(str(test.iloc[x]['user']) + '\t' + str(test.iloc[x]['venue']) + '\t' + '1'
                + '\t' + str(test.iloc[x]['time']) + '\t' + str(test.iloc[x]['photo']) + '\n')

print('sucessfully save test.tsv')

trainPlusTest=pd.concat([train,test])

with open('all.tsv','w') as f:
    for x in range(len(trainPlusTest)):
        f.write(str(trainPlusTest.iloc[x]['user'])+'\t'+str(trainPlusTest.iloc[x]['venue'])+'\t'+'1'
        +'\t'+str(trainPlusTest.iloc[x]['time'])+ '\t' + str(trainPlusTest.iloc[x]['photo'])+'\n')



userVenueSet=set()
userVenueDict=dict()
venueSet=set([i for i in range(venueNum)])
for x in range(len(trainPlusTest)):
    if trainPlusTest.iloc[x]['user'] not in userVenueDict:
        userVenueDict[trainPlusTest.iloc[x]['user']]=set()
    userVenueDict[trainPlusTest.iloc[x]['user']].add(trainPlusTest.iloc[x]['venue'])



with open('test.negative.tsv','w') as f:
    for x in range(len(test)):
        if test.iloc[x]['user'] in userVenueDict:
            m=list(venueSet-userVenueDict[test.iloc[x]['user']])
        else:
            m=[]
        random.shuffle(m)
        r=50
        if len(m)<r:
            r=len(m)
        f.write('('+str(test.iloc[x]['user']) + ',' + str(test.iloc[x]['venue'])+')')
        for y in range(r):
            f.write('\t'+str(m[y]))
        f.write('\n')

print('sucessfully save test.negative.tsv')



