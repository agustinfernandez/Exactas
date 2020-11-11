#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 12:23:32 2020

@author: agustin18
"""

def jugar(m):
    w=0
    suma=0
    while suma<21:
    
        suma=suma+m.pop(0)
        w=w+1
        
    return suma

res=jugar(mazo)
print(res)

    def generar_mazo(n):
    
        mazo=[]
        
        z=0
        while z<5:
            z=z+1
            
            x=0
            while x<4:
                x=x+1
            
                i=0
                while i<13:
                
                    i=i+1
                    mazo.append(i)
            
                
        return mazo
    
    cantidad_jug= 5
    mazo=generar_mazo(cantidad_jug)
    
