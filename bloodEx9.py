import numpy as np
import matplotlib.pyplot as plt
import pandas as df
import numpy.polynomial.polynomial as poly
from plotnine import *

###Problem 1
stuff = []
with open('Book2.txt','r') as f:
    for line in f:
        info = line.rstrip() 
        stuff.append(info)

count = 0
x = []
y1= []
y2 =[]
for line in stuff:
    if count:
        v1,v2,v3 = line.split('\t')
        x.append(int(v1))
        y1.append(float(v2))
        y2.append(float(v3))
    count +=1
print x
fig, ax1 = plt.subplots()
plt.plot(x,y1,'r.')
plt.xlabel('Year')
plt.ylabel('Divorce rate in Maine per 1000')
plt.legend(['Divorce'])
coefs = poly.polyfit(x, y1, 4)
ffit = poly.polyval(x, coefs)
plt.plot(x, ffit, 'r')

ax2=ax1.twinx()
plt.plot(x,y2,'g.')
plt.ylabel('Per capita margarine consumption(pounds)')
plt.legend(['Margarine'],loc=1,bbox_to_anchor=[0,.9,1.01,0])
coefs = poly.polyfit(x, y2, 4)
ffit = poly.polyval(x, coefs)
plt.plot(x, ffit, 'g')


###Problem 2
data = df.read_csv('data.txt')
dirs = []

for i in range(len(data.iloc[:,0])):
    if data.iloc[i,0] not in dirs:
        dirs.append(data.iloc[i,0])
n = data[data['region']==dirs[0]]
e = data[data['region']==dirs[1]]
s = data[data['region']==dirs[2]]
w = data[data['region']==dirs[3]]
plt.figure()
plt.bar(dirs,[float(n.mean()),float(e.mean()),float(s.mean()),float(w.mean())])

p = ggplot(data, aes('region', 'observations'))+geom_jitter()
p.draw()
