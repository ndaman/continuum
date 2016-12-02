# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:46:00 2012

@author: smit1447
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fmin

data = np.loadtxt('char_dat.txt')

newdata = []
dats = -1
temps = []

for i in xrange(len(data)):
    if data[i,0] != 0:
        newdata.append([(data[i,1],data[i,2])])
        dats += 1
        temps.append(data[i,0])
    else:
        newdata[dats].append((data[i,1],data[i,2]))

#plot data on same time scale
plt.figure()
for i in newdata:
    plt.plot([x[0] for x in i],[x[1] for x in i])
plt.xlabel('Log(t)')
plt.ylabel('Log(E)')
plt.show()

#manually shift times for each temperature so that they line up
#use 0 for reference temperature, shift other values
plt.figure()
at = [-5,-4,-3.5,-2.4,-2,-1.5,0,1.5,2.2,2.8,3.6,4.3]
for i in xrange(len(newdata)):
    plt.plot([float(x[0]+at[i]) for x in newdata[i]],[x[1] for x in newdata[i]])
plt.xlabel('Log(t)')
plt.ylabel('Log(E)')


x0 = [17.4,51.6] #initiial values for optimization
t = np.array(temps)-150.8 #convert absolute temps to relative
a = np.array(at) #manual shift values
#Arrhenius function to model temperature shift factor
def myfunc(x):
    ans = x[0]*t[1:]/(x[1]+t[1:])
    return sum((a[1:]-ans)**2)
#optimize constants in Arrhenius function
ans = fmin(myfunc,x0)
plt.figure()
plt.plot(t,a,'ko')
plt.plot(t,ans[0]*t/(ans[1]+t),'r--')
plt.ylabel(r'Log($a_t$)')
plt.xlabel('T-$T_{ref}$')
print ans
plt.show()
