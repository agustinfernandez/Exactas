#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:49:33 2020

@author: agustin18
"""
import random

import numpy as np

album=[0,0,0,0,0,0]

def hayalguno(album,e):
    res=False

    i=0
    while i<len(album):
        
        if album[i]==e:
            
            res=True
            
        i=i+1
       
    return res

hay=hayalguno(album,0)
#print (hay)
            
def comprar_una_figu(figus_total):
    x=0
    z=figus_total
    y=random.randint(x, z)
    return y

comprar=comprar_una_figu(len(album))
print(comprar)

def cuantas_figus(figus_total):
    i=0
    count=0
    while i<len(album):
        if album[i]!= comprar:
            album[i]=comprar
        i=i+1
        count=count+1
        print(count)
    return count
figus_total=len(album)
cuanta=cuantas_figus(figus_total)
print(cuanta)








