#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:36:55 2020

@author: agustin18
"""
import random
def generar_bosque(n):

    bosque=[]
    while len(bosque)<n:
        bosque.append(0)
        
    return bosque
def suceso_aleatorio(p):
    
    if random.random()<=p:
        res= True
    else:
        res= False
    return (res)
    
def brotes(bosque,p):
    i=0
    while i<len(bosque):
        if suceso_aleatorio(p):
            bosque[i]=1
            
        i=i+1
    return bosque
#bosque= generar_bosque(10)
#print(bosque)
#bosque=brotes(bosque,0.6)
#print(bosque)

def cuantos(bosque, tipo_celda):
    res= bosque.count(0)
    return res

def rayos(bosque, f):
    i=0
    while i<len(bosque):
        if suceso_aleatorio(f) and bosque[i]==1:
            bosque[i]=-1
        i=i+1
       
    return bosque
#bosque=rayos(bosque,0.2)
#print(bosque)

def propagacion(bosque):
    i=1
    while i<len(bosque)-1:
        if bosque[i]==1 and (bosque[i+1]==-1 or bosque[i-1]==-1):
            bosque[i]=-1
        i=i+1
    
    
    j=len(bosque)-2
    while j>0:
        if bosque[j]==1 and (bosque[j+1]==-1 or bosque[j-1]==-1):
            bosque[j]=-1
        j=j-1
    
    if bosque[0]==1 and bosque[1]==-1:
        bosque[0]=-1
    if bosque[len(bosque)-1]==1 and bosque[len(bosque)-2]==-1:
        bosque[len(bosque)-1]=-1
    return bosque
b_1 = [1, 1, 1, -1, 0, 0, 0, -1, 1, 0]
print(b_1)
res=propagacion(b_1) 
print(res)      
            
            
        
    

        
        
    
