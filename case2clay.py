# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 14:35:39 2017

@author: sandhya
"""

import math
import matplotlib.pyplot as plt
import numpy
d = 60
EI = 93e10
L = 38
e = 12
c = 13.888889# in lb/in2
gamma = 0.034722# in lb/in3
num = 125*math.pow(c,1.5)*math.pow((EI*gamma*d),0.5)/(math.pow((1+(e/d)),1.5))
print(num)
Pt = [20000,40000,80000,120000,160000]
Peg = [0]
nhg = [0]
Tg = []
ygg = [0]
Mmax = [0]
[Peg.append(item/1000) for item in Pt]
for i in range(len(Pt)):
    nh = num/math.pow(Pt[i],1.5)
    T = math.pow((EI/nh),(1/5))
    Pei = Pt[i]*(1+(0.67*e/T))
    Pe = Pt[i]
    Ti = 0
    n = 0
    while((abs(Pe-Pei)>0.000001)and(abs(T-Ti)>0.000001)):
        nh = num/math.pow(Pei,1.5)
        Ti = T    
        T = math.pow((EI/nh),(1/5))
        Pei = Pe
        Pe = Pt[i]*(1+(0.67*e/T))
    nhg.append(nh)
    Tg.append(T)
    yg = 2.43*Pe*math.pow(T,3)/EI#in in
    ygg.append(yg)
print(nhg)
plt.plot(ygg,Peg,'ro--')
plt.axis([0, 0.5, 0, 200])
plt.xlabel('Groundline displacement,in')
plt.ylabel('Lateral load,kips')
plt.grid()
plt.show()
plt.plot(ygg[1:(len(Pt)+1)],nhg[1:(1+len(Pt))],'bo--')
plt.axis([0, 0.5, 0, 2000])
plt.xlabel('Maximum Moment')
plt.ylabel('Lateral load,kips')
plt.grid()
plt.show()