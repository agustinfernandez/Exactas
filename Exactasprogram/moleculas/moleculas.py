#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:12:05 2020

@author: agustin18
"""


min_x= 0
max_x=20
max_y=20
min_y=0
pos_x=10
pos_y=10
pasos_totales=100
dt=2
vel_x=1
vel_y=1

# nueva_x=pos_x[0]+vel_x*dt
# nueva_y=pos_y[0]+vel_y*dt

# if pos_x>max_x :
#     vel_x=-vel_x
#     pos_x=pos_x-2*(pos_x-max_x )

# if pos_x<min_x:
#     vel_x=-vel_x
#     pos_x=pos_x-2*(pos_x-min_x)
    
def rebotar(pos,vel,minimo,maximo):
    if pos>maximo :
        vel=-vel
        pos=pos-2*(pos-maximo)

    if pos<minimo:
        vel=-vel
        pos=pos-2*(pos-minimo)
    
    return [pos,vel]

def mover_particula(pos_x,pos_y,vel_x,vel_y,dt,minimo_x,maximo_x,minimo_y,maximo_y):
    
    prox_x=pos_x+vel_x*dt
    rebo=rebotar(prox_x, vel_x, minimo_x, maximo_x)
    xfinal=rebo[0]
    vxfinal=rebo[1]
    
    prox_y=pos_y+vel_y*dt
    reboy=rebotar(prox_y, vel_y, minimo_y, maximo_y)
    yfinal=reboy[0]
    vyfinal=reboy[1]
    
    return [xfinal,yfinal,vxfinal,vyfinal]
    
mov=mover_particula(pos_x,pos_y,vel_x,vel_y,dt,min_x,max_x,min_y,max_y)    
        
print(mov)

listaX=[]
listaX.append(pos_x)
listaY=[]
listaY.append(pos_y)
listavelX=[]
listavelX.append(vel_x)
listavelY=[]
listavelY.append(vel_y)

for i in range(pasos_totales):
    mover=mover_particula(listaX[i],listaY[i],listavelX[i],listavelY[i],dt,min_x,max_x,min_y,max_y)
    listaX.append(mover[0])
    listaY.append(mover[1])
    listavelX.append(mover[2])
    listavelY.append(mover[3])
    

print(listaX)



    
    