# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:46:00 2012

@author: smit1447
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fmin
from scipy import interpolate
import pandas as pd #to read excel sheets
#new plot style
plt.style.use('ggplot')

#load all sheets into data array
data = pd.read_excel('temperature_data.xlsx',sheetname=range(9))
#get header values
head = data[1].columns.values
#get temperature values
temps = [int(i) for i in pd.ExcelFile('temperature_data.xlsx').sheet_names]

#plot all temperature ranges on same axis
plt.figure()
for i in range(9):
    #this if/esle is just an easy way to get all lines on same figure
    if (i == 0):
        ax = data[i].plot(x=head[0],y=head[1],logx=True, logy=True,label=temps[i])
    else:
        data[i].plot(x=head[0],y=head[1],ax=ax,logx=True, logy=True,label=temps[i])
ax.set_ylabel('J (GPa$^{-1}$)')
ax.set_ylim([1,20])
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
#plt.savefig('original.png',frameon=False,bbox_inches='tight')

#array of shifts
at = [0] #initial value of 0
#will find incremental shifts between to adjacent curves
for i in range(8):
    #create arrays, operate in logspace
    x0 = np.log10(np.array(data[i][head[0]]))
    y0 = np.log10(np.array(data[i][head[1]]))
    #interpolation function, inverted so we can compare y-values and find x-shift
    f0 = interpolate.interp1d(y0, x0)
    x1 = np.log10(np.array(data[i+1][head[0]]))
    y1 = np.log10(np.array(data[i+1][head[1]]))
    f1 = interpolate.interp1d(y1, x1)
    #find shift at mean y0 value
    avg = np.mean(y0)
    at.append(f0(avg) - f1(avg))
#cumulative sum of incremental shifts
at = np.cumsum(at)
at
#adjust shift to desired reference
ref = 1 #python indexes start at 0, 1 corresponds to T = 20
at = at - at[ref]
at
#check plot
plt.figure()
for i in range(9):
    plt.loglog(data[i][head[0]]*10**at[i],data[i][head[1]],label=temps[i])
plt.ylabel('J (GPa$^{-1}$)')
plt.xlabel('t (sec.)')
plt.ylim([1,20])
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
#plt.show()
plt.savefig('shifted.png',frameon=False,bbox_inches='tight')


x0 = [17.4,51.6] #initiial values for optimization
t = np.array(temps)-20.0
a = np.array(at) #shift values
#WLF function to model temperature shift factor
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

#use WLF shift function instead of manual shift
plt.figure()
for i in range(9):
    a = ans[0]*t[i]/(ans[1]+t[i])
    plt.plot(np.log(data[i][head[0]])+a,np.log(data[i][head[1]]),label=temps[i])
plt.ylabel('log(J) (GPa$^{-1}$)')
plt.xlabel('log(x) (s)')
plt.ylim([0,3])
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
