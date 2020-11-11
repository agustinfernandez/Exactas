#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:48:17 2020

@author: agustin18
"""
import random

def generar_bosque(n):

    bosque=[]
    while len(bosque)<n:
        bosque.append(0)

    return bosque
bosque=generar_bosque(100)
print(bosque)
def suceso_aleatorio(p):

    if random.random()<=p:
        res= True
    else:
        res= False
    return (res)

res=suceso_aleatorio(0.1)

def brotes(bosque,p):
    i=0
    while i<len(bosque):
        if suceso_aleatorio(p):
            bosque[i]=1
            
            i=i+1
    return bosque

bosque=brotes(bosque,0.1)
print (bosque)
def cuantos(bosque, tipo_celda):
    res= bosque.count(0)
    return res