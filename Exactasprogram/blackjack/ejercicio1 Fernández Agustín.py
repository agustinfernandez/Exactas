# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
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


    def jugar(m):
        i=0
        suma=0
        while suma<21:
        
            suma=suma+m.pop(0)
            i=i+1
            print(m)
        return suma
    
    
    res=jugar(mazo)
    print(res)