#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:02:27 2020

@author: agustin18
"""

import numpy as np


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
tablero=crear_tablero(7)
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
print (tablero)

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
    if es_borde(tablero,(x,y+1))==False:
        vecinos.append((x,y+1))
    return vecinos

vecin=vecinos_de(tablero,(5,5))
print (vecin)

def desbordar_posicion(tablero, coord):
    if tablero[coord]==4:
        tablero[coord]=tablero[coord]-4
    
        z=0
        while z<len(vecinos_de(tablero,coord)):
            tirar_copo(tablero,vecinos_de(tablero,coord)[z])
            z=z+1
        
    return tablero

desborde=desbordar_posicion(tablero, (5,5))
print (desborde)


def desbordar_arenero(tablero):
    
    cantidad_filas = tablero.shape [0]
    cantidad_columnas = tablero.shape [1]
    for k in range (1 , cantidad_filas - 1):
        for j in range (1 , cantidad_columnas - 1) :
            desbordar_posicion(tablero, (k,j) )
    return tablero

def hay_que_desbordar(tablero):
    res= False
    for w in range(1, tablero.shape[0]-1):
        for d in range (1,tablero.shape[1]-1):
            if tablero[(w,d)]>=4:
                res=True
    return res

    
def estabilizar(tablero):
    while hay_que_desbordar (tablero)==True:
        
        desbordar_arenero (tablero)
    return tablero

    
def paso(tablero):
    tirar_copo(tablero, (tablero.shape[0]//2, tablero.shape[1]//2))
    estabilizar(tablero)
    return tablero
pas=paso(tablero)
print(tablero)
    
        



    
    

