#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pandas as pd
import numpy
import pickle

#一个用户可能在一个景点发很多图片，后缀ByPhotos表示按图片统计，ByVenues表示按景点统计，
venue_id=[]         #景点ID
categories=[]       #标签的景点数
categories_num=[]   #景点的标签数
userVenueByPhotos=[]       #照片的user,景点
tip_user=[]         #tip的user,景点
usrByPhotos=[]
plaByPhotos=[]
userid=[]           #大于10的用户ID
venueid=[]          #大于10的地点ID
folders=['1-500','500-2000','2000-5000','5000-10000','Supplements']
photos=[]
'''
for m in folders:
    # with open('venues'+str(m)+'.json','r',encoding="utf8") as file:
    #     for line in file.readlines():
    #         venue=json.loads(line)['venue']
    #         for i in range(0, len(venue['categories'])):
    #             categories.append(venue['categories'][i]['id'])
    #         categories_num.append(len(venue['categories']))
    #         venue_id.append(venue['id'])

    with open(m+'/photosData.json','r',encoding="utf8") as file:
        for line in file.readlines():
            userVenueByPhotos.append([json.loads(line)['photo']['user']['id'],json.loads(line)['id']])
            usrByPhotos.append(json.loads(line)['photo']['user']['id'])
            plaByPhotos.append(json.loads(line)['id'])
            photos.append(json.loads(line)['photo']['id'])
        print("load %s successfully"%{m})

'''

# with open('params.sav', 'wb') as f:
#     pickle.dump([userVenueByPhotos,usrByPhotos,plaByPhotos,photos], f, -1)

print('save params successfully')
params=[]
with open('params.sav', 'rb') as f:
    tmp = pickle.load(f)
    userVenueByPhotos, usrByPhotos, plaByPhotos,photos=tmp
userVenueByVenues=set() # 用户景点set
for pu in userVenueByPhotos:
    pu=tuple(pu)
    userVenueByVenues.add(pu)

usersByVenues=[]
for m in userVenueByVenues:
    usersByVenues.append(m[0])


userNumByVenues=list(zip(*numpy.unique(usersByVenues, return_counts=True)))
userNumByPhotos=list(zip(*numpy.unique(usrByPhotos, return_counts=True)))
plaNumByPhotos=list(zip(*numpy.unique(plaByPhotos, return_counts=True)))

#筛选出去过景点数大于20（即图片数肯定更多）的用户
for p in range(1,len(userNumByVenues)):
    if userNumByVenues[p][1] >=20:
        userid.append(userNumByVenues[p][0])


#再筛选出图片数大于x的景点
for p in range(1,len(plaNumByPhotos)):
    if plaNumByPhotos[p][1] >=50:
        venueid.append(plaNumByPhotos[p][0])




# print(dict(zip(*numpy.unique(categories, return_counts=True))))    #标签的景点数
# print(dict(zip(*numpy.unique(categories_num, return_counts=True))))#景点的标签数
# lab=dict(zip(*numpy.unique(categories, return_counts=True))).values()
# print(lab)



userVenueByPhotos=numpy.array(userVenueByPhotos)
user_label=numpy.unique(userVenueByPhotos[:,0])
venue_label=numpy.unique(userVenueByPhotos[:,1])
a=list(zip(*numpy.unique(userVenueByPhotos[:,0], return_counts=True)))
b=list(zip(*numpy.unique(userVenueByPhotos[:,1], return_counts=True)))
a=numpy.array(a)[:,1]
b=numpy.array(b)[:,1]
a=list(zip(*numpy.unique(a, return_counts=True)))
b=list(zip(*numpy.unique(b, return_counts=True)))
a=numpy.array(a)
b=numpy.array(b)
a1=list(a[:,0])
a2=list(a[:,1])
b1=list(b[:,0])
b2=list(b[:,1])



file_obj = open("distribution.txt", 'w')
for num in a1:
    file_obj.writelines(num)
    file_obj.writelines(', ')
file_obj.write('\n\n')
for num in a2:
    file_obj.writelines(num)
    file_obj.writelines(', ')
file_obj.write('\n')
file_obj.write('\n')
for num in b1:
    file_obj.writelines(num)
    file_obj.writelines(', ')
file_obj.write('\n\n')
for num in b2:
    file_obj.writelines(num)
    file_obj.writelines(', ')
file_obj.write('\n')

file_obj.close()


# with open('tipsData.json','r',encoding="utf8") as file:
#     for line in file.readlines():
#         tip_user.append([json.loads(line)['tip']['user']['id'], json.loads(line)['id']])
#
# tip_user=numpy.array(tip_user)
# user_label=numpy.unique(tip_user[:,0])
# venue_label=numpy.unique(tip_user[:,1])
# print('tip')
# print(len(user_label))
# print(len(venue_label))

'''
matrix=numpy.zeros((len(user_label),len(venue_label)))
print(numpy.sum(matrix))


for k in range(0,len(tip_user)):
    data=tip_user[k]
    i=user_label.tolist().index(data[0])
    j=venue_label.tolist().index(data[1])
    matrix[i,j]=matrix[i,j]+1
print(numpy.sum(matrix))
'''


# df=pd.DataFrame(matrix,columns=venue_label,index=user_label)
# df.to_csv('Data analysis result.csv')



n=0
nn=0
file_write_obj = open("photo,user,venue,time.txt", 'w')
for m in folders:
    with open(m+'/photosData.json','r',encoding="utf8") as file:
        for line in file.readlines():
            nn = nn + 1
            if json.loads(line)['photo']['user']['id'] in userid:
                if json.loads(line)['id'] in venueid:
                    puvt = json.loads(line)['photo']['id'] +', '+ json.loads(line)['photo']['user']['id'] + ', '+ json.loads(line)['id']  + ', ' +  str(json.loads(line)['photo']['createdAt'])
                    file_write_obj.writelines(puvt)
                    file_write_obj.write('\n')
                    n=n+1
    print("secondly load %s successfully" % {m})
print('地点剩余 ',len(venueid),'/',len(plaNumByPhotos))
print('用户剩余 ',len(userid),'/',len(userNumByPhotos))
print('photo剩余 ',n,'/',nn)
file_write_obj.close()
print('稀疏性=',1-(n/(len(userid)*len(venueid))))