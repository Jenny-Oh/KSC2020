#-*coding:utf-8-*-
import math
import pprint as p
import random as r
import json
from operator import itemgetter

max_lat = 89.9993137156
min_lat = -36.086009
max_lon = 115.086769
min_lon = -142.466649843

d_lat = (max_lat-min_lat)/3
d_lon = (max_lon-min_lon)/3

lat_list = [min_lat, min_lat + d_lat, max_lat - d_lat, max_lat]
lon_list = [min_lon, min_lon + d_lon, max_lon - d_lon, max_lon]

point = list()

for lat in lat_list:
    for lon in lon_list:
        point.append((lat,lon))

del point[0]
del point[3-1]
del point[12-2]
del point[15-3]

#p.pprint(point)

idx = 0
tmp_dataset = list()
#데이터 셋 리스트 = [id, apha(선호도), lat, lon]
for i in range(1,10):
    for item in point:
        element = list()
        element.append(int(idx))
        element.append(i/10)
        element.append(item[0])
        element.append(item[1])
        idx = idx+1
        tmp_dataset.append(element)

dataset = r.sample(tmp_dataset,100)
dataset.sort(key = itemgetter(0))

i = 0
for lists in dataset:
    lists[0] = i
    i = i+1
#print(dataset)

data_group = dict()

for datas in dataset:
    data_dict = dict()
    data_dict['id']=datas[0]
    data_dict['alpha']=datas[1]
    data_dict['lat'] = datas[2]
    data_dict['lon'] = datas[3]
    name = datas[0]
    data_group[name] = data_dict

with open('dataset.json','w',encoding="utf-8") as mfile:
    json.dump(data_group,mfile,ensure_ascii=False, indent="\t")