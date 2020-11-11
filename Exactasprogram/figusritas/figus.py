#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:03:29 2020

@author: agustin18
"""

import random
import numpy as np
album =[0, 0, 0, 0, 0, 0]



def comprar_una_figu(figus_total):
    a=0
    b=figus_total
    r=random.randint(a, b)
    return r
res=comprar_una_figu(len(album))

def cuantas_figus(figus_total):

    count=0
    album[i]==res
    for i in range(len(figus_total)):
        if album[i]!=res:
            album[i]= res
    count=count+1     
    return  album


res=cuantas_figus(len(album))