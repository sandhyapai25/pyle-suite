# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 10:04:54 2017

@author: sandhya
"""

import math
import matplotlib.pyplot as plt
import numpy
d = 10
EI = 38e8
L = 115
e = 12
c = 4.16667# in lb/in2
gamma = 0.0636574# in lb/in3
My = 116
num = 125*math.pow(c,1.5)*math.pow((EI*gamma*d),0.5)/(math.pow((1+(e/d)),1.5))
Pt = [5000,10000,15000,20000,25000]
Peg = [0]
nhg = []
Tg = []
ygg = [0]
Mmax = [0]
[Peg.append(item/1000) for item in Pt]
print(Peg)
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
    Mmax.append(0.77*Pe*T/12000)    
    yg = 2.43*Pe*math.pow(T,3)/EI#in in
    ygg.append(yg)
print(Mmax)
plt.plot(ygg,Peg,'ro--')
plt.axis([0, 8, 0, 25])
plt.xlabel('Groundline displacement,in')
plt.ylabel('Lateral load,kips')
plt.grid()
plt.show()
line = plt.plot(Mmax,Peg,'bo--')
Pu = print(numpy.interp([My],Mmax,Peg))
plt.axis([0, 200, 0, 25])
plt.xlabel('Maximum Moment')
plt.ylabel('Lateral load,kips')
plt.grid()
plt.show()
