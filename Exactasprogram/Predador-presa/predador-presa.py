# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np



def crear_tablero(filas,columnas):
    t = np.repeat(" ",(filas+2)*(columnas+2)).reshape (filas+2 ,columnas+2)
    
    i=0
    while i<t.shape[1]:
        t[(0,i)]= "M"
        t[(t.shape[0]-1,i)]="M"
        i=i+1
    i=0
    while i<t.shape[0]: 
        t[(i,0)]="M"
        t[(i,t.shape[1]-1)]="M"
        i=i+1
    return t
t=crear_tablero(3,4)
#print(t) 

filas= [1 , 2 , 2 , 3 , 1]
columnas= [3 , 1 , 3 , 1 , 1]
animal=["A", "A" , "A" , "A" , "L" ]
for i in range(len(animal)):
    t [(filas[i] , columnas[i])] = animal[i]
    
    
print(t)



def es_borde(tablero,coord):
   
    if tablero[coord]=="M":
        a=True
    else:
        a=False
    return a

    
def vecinos_de(tablero,coord):
    x=coord[0]
    y=coord[1]
    vecinos=[]
    
    if es_borde(tablero,(x-1,y-1))==False:
        vecinos.append((x-1,y-1)) 
    if es_borde(tablero,(x-1,y))==False:
        vecinos.append((x-1,y))   
    if es_borde(tablero,(x-1,y+1))==False:
        vecinos.append((x-1,y+1))
        
    if es_borde(tablero,(x,y+1))==False:
        vecinos.append((x,y+1))
        
    
    if es_borde(tablero,(x+1,y+1))==False:
        vecinos.append((x+1,y+1))
        
    if es_borde(tablero,(x+1,y))==False:
        vecinos.append((x+1,y))   
    
    if es_borde(tablero,(x,y-1))==False:
        vecinos.append((x,y-1))
    
       
    
    return vecinos

vecin=vecinos_de(t,(3,3))
    
#print(vecin)    


def buscar_adyacente(tablero,coord,objetivo):
    
    
    vecino=[]
    alrededor=vecinos_de(tablero,coord)
    z=0
    while z < len(alrededor):
        if tablero [alrededor[z]] == objetivo:
            vecino.append(alrededor[z])
            
        z=z+1
    if len(vecino)>0:
        return vecino[0]
    return vecino
        
adya=buscar_adyacente(t,(1,1),"A")            
    
    
def mover(tablero,coord):
    
    ady=buscar_adyacente(tablero,coord," ")
    
    
    
    if ady!=[]:
       tablero[ady]=tablero[coord]
       tablero[coord]=" "
    return tablero

move=mover(t,(1,1))
    
print(move)
    
def alimentar(tablero,coord):
    adye=buscar_adyacente(tablero,coord,"A")
    if tablero[coord]=="L" and adye!=[]:
        tablero[adye]=tablero[coord]
        tablero[coord]=" "
    return tablero
        

alim=alimentar(t,(1,2))

print(alim)     
        
def reproducir(tablero,coord):
    adya=buscar_adyacente(tablero,coord,"A")
    adyac=buscar_adyacente(tablero,coord,"L")
    ad=buscar_adyacente(tablero,coord," ")
    
    if tablero[coord]=="A" and adya!=[]:
        tablero[ad]="A"
        
    if tablero[coord]=="L" and adyac!=[]:
        tablero[ad]="L"
    
    return tablero

rep=reproducir(t,(1,1))
        
print(rep)
    
def fase_mover(tablero):
    cantidad_filas = tablero.shape [0]
    cantidad_columnas = tablero.shape [1]
    for k in range (1 , cantidad_filas - 1):
        for j in range (1 , cantidad_columnas - 1) :
            mover(tablero, (k,j) )   
    
    return tablero


def fase_alimentacion(tablero):
    cantidad_filas = tablero.shape [0]
    cantidad_columnas = tablero.shape [1]
    for w in range (1 , cantidad_filas-1):
        for q in range (1 , cantidad_columnas-1) :
            alimentar(tablero,(w,q) )   
    
    return tablero

def fase_reproduccion(tablero):
    cantidad_filas = tablero.shape [0]
    cantidad_columnas = tablero.shape [1]
    for c in range (1 , cantidad_filas - 1):
        for x in range (1 , cantidad_columnas - 1) :
            reproducir(tablero, (c,x) )   
    
    return tablero



def evolucionar(tablero):
    fase_alimentacion(tablero)
    print(tablero)
    fase_reproduccion(tablero)
    print(tablero)
    fase_mover(tablero)
    print(tablero)
    return tablero

evo=evolucionar(t)
print(evo)

def evolucionar_en_el_tiempo(tablero,p):
    d=0
    while d<p:
        evolucionar(tablero)
        d=d+1
    return tablero

evolu=evolucionar_en_el_tiempo(t,3)



    