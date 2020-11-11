#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:02:27 2020

@author: agustin18
"""

import numpy as np
import matplotlib.pyplot as plt

#t = np.repeat(0 ,8*8).reshape (8 ,8)
##print t
#
#i=0
#while i<t.shape[0]:
#    t[(0,i)]=-1
#    t[(t.shape[0]-1,i)]=-1
#    t[(i,0)]=-1
#    t[(i,t.shape[0]-1)]=-1
#    i=i+1


#Implemente una función crear_tablero(n) que reciba como entrada la cantidad n de filas y columnas
#del valle, y devuelva un tablero vacı́o (0 en todas posiciones utilizables) y el valor -1 en los bordes.

def crear_tablero(n):
    t = np.repeat(0 ,n*n).reshape (n ,n)
    
    i=0
    while i<t.shape[0]:
        t[(0,i)]=-1
        t[(t.shape[0]-1,i)]=-1
        t[(i,0)]=-1
        t[(i,t.shape[0]-1)]=-1
        i=i+1
    return t
tablero=crear_tablero(8)
print(tablero)        
#    
#def crear_tablero(n):
#    t = np.repeat(0 ,n*n).reshape (n ,n)
#    
#    i=0
#    while i<t.shape[0]:
#        t[(0,i)]=-1
#        t[(t.shape[0]-1,i)]=-1
#        t[(i,0)]=-1
#        t[(i,t.shape[0]-1)]=-1
#        i=i+1
#    return t
#tablero=crear_tablero(7)
#print(tablero)        
#    
def es_borde(tablero,coord):
   
    if tablero[coord]==-1:
        a=True
    else:
        a=False
    return a

res=es_borde(tablero, (1,6))

#Implementar una función tirar_copo(tablero, coord) que tome como entrada un tablero, la coor-
#denada (i,j) de la posición donde cae, y agregue un copo en ese lugar (es decir, incremente la
#cantidad de copos en esa posición).
       
def tirar_copo(tablero,coord):
    
    tablero[coord]=tablero[coord]+1
    

tirar_copo(tablero,(5,5))
print tablero

def vecinos_de(tablero,coord):
    x=coord[0]
    y=coord[1]
    vecinos=[]
    
    if es_borde(tablero,(x-1,y))==False:
        vecinos.append((x-1,y))   
    if es_borde(tablero,(x+1,y))==False:
        vecinos.append((x+1,y))
    if es_borde(tablero,(x,y-1))==False:
        vecinos.append((x,y-1))
    if es_borde(tablero,(x,y-1))==False:
        vecinos.append((x,y-1))
    return vecinos

vecin=vecinos_de(tablero,(5,5))
print (vecin)
        



    
    

