#!/usr/bin/python3
import os
import json

it = []
_dir = 'obnote01'
for p,d,f in os.walk(_dir):
    for i in f:
        if '.md' in i:
            fpath = (p + '/' + i).split('/')
            it.append(fpath)
            #print(fpath)

dt = {}
for i in it:
    if len(i) >= 4:
        d1 = i[1]
        d2 = i[2]
        f = '/'.join(i[3:])
        if d1 not in dt:
           dt[d1] = {}
        if d2 not in dt[d1]:
           dt[d1][d2] = {}
        dt[d1][d2][f] = '/'.join(i)

#print(json.dumps(dt, indent=2))
ds = open('_sidebar.md','w')
for k,v in dt.items():
    ds.write( '\n - {}\n'.format(k))
    for i,i2 in v.items():
        ds.write( '   - {}\n\n'.format(i))
        for j in i2:
            ds.write( '     - [{}]({}/{})\n'.format(j.replace(' ','%20').replace('.md',''),_dir,(k+'/'+i+'/'+j).replace(' ','%20')))
        ds.write('\n')
    ds.write('\n')
print('done...')

