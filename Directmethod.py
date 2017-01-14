# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 17:04:34 2017

@author: Lenovo pc
"""

import math
d = 24 
EI = 4.854e10
L = 69
e = 12
phi = 39
gamma = 0.0382 
My = 7e6
Pt = 10000
To = 0
Cphi = 3*(math.pow(1.316,phi))/100000
num = 150*Cphi*(math.pow(gamma,1.5))*(math.pow((EI*d),0.5))
# Since T is not known to start with, assume e = 0, and Pe = Pt= 10,000 Ibs
nh = num/Pt
T = math.pow((EI/nh),(1/5))
Pe = Pt*(1+(0.67*e/T))
while(((Pe-Pt)>(10^-1))and((T-To)>(10^-1))):
    Pt = Pe
    To = T
    nh = num/Pe
    T = math.pow((EI/nh),(1/5))
    Pe = Pt*(1+(0.67*e/T))
    print(T)
    print(Pe)
    print(Pe-Pt)
    break