#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:03:29 2020

@author: agustin18
"""

import random
import numpy as np
album =[0,0, 0, 0, 0, 0]


def comprar_una_figu(figus_total):
    a=0
    b=figus_total
    r=random.randint(a, b)
    return r
x=comprar_una_figu(len(album))
print(x)

def cuantas_figus(figus_total):
    i=0
    count=0
    while i<len(album):
        if [i]!= x:
            i=x
        i=i+1
    count=count+1
    return count

res= cuantas_figus(x)
print(x)    
    
    

   
