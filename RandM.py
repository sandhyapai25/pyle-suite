# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:06:26 2017

@author: Lenovo pc
"""
import math
EI = float(input("Enter Flexural Rigidity of Pile material"))
nh = float(input("Enter Coefficient of soil modulus variation"))
Pt = float(input("Enter Lateral load at pile head"))
Mt = float(input("Enter Lateral moment at pile head"))
EInh = EI/nh
T=math.pow(EInh,(1/5))
Ay = float(input("Enter Non-dimensional coefficient Ay"))
By = float(input("Enter Non-dimensional coefficient By"))
y = (Ay*(Pt*math.pow(T,3)/EI))+(By*(Mt*math.pow(T,2)/EI))