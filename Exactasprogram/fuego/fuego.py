#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:36:55 2020

@author: agustin18
"""
import random
import numpy as np 

def generar_bosque(n):
    
    bosque=[]
    while len(bosque)<n:
        bosque.append(0)

    return bosque
bosque=generar_bosque(100)

def suceso_aleatorio(p):    
    if random.random()<=p:
        res= True
    else:
        res= False
    return (res)

def brotes(bosque, p):
    i=0
    while i<len(bosque):
        if suceso_aleatorio(p):
            bosque[i]=1  
        i=i+1
    return bosque

def incendio_forestal(n_rep):
    
    sobreviven = []
    
    bosque=generar_bosque(100)
    print(bosque)
    
    z=0
    while z< n_rep:
        
        res=suceso_aleatorio(0.6)
        
        
    
        bosque=brotes(bosque,0.6)
        #print (bosque)
        

        def rayos(bosque, f):
            i=0
            while i<len(bosque):
                if suceso_aleatorio(f) and bosque[i]==1:
                    bosque[i]=-1
                i=i+1
       
            return bosque
        bosque=rayos(bosque,0.2)
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
    
        bosque=propagacion(bosque) 
        #print(bosque)      
    
    
        def limpieza(bosque):
            i=0
            while i<len(bosque):
                if bosque[i]==-1:
                    bosque[i]=0
                i=i+1
            
        limpieza(bosque)
        #print(bosque)
        
        def cuantos(bosque, tipo_celda):
            cuenta= bosque.count(tipo_celda)
            return cuenta
        
        
        
        sobreviven.append( cuantos(bosque,1))
            
        
        
    
        z=z+1
        
    print(sobreviven)
    resultado = np.mean(sobreviven)    
    return resultado

n_rep=50
media =incendio_forestal(n_rep)
print(media)
            
            
    
    
        
            
        
    
            
            
        
