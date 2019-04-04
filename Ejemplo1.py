# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 2019

@author: Nahuel
"""
# la variable veces especifica cada cuantas muestras se quiere hacer el promedio
def MediaMovil(vector, veces):
    prom = [];
    k = 0;
    iteraciones = len(vector) - veces + 1;
    for i in range(iteraciones):
        acum = 0;
        for j in range(k,k+veces):
            acum = acum + vector[j];
        prom.append(acum/veces);
        k = k+1;
    print(prom);    

p1 = [11, 12, 13, 14, 15, 16, 17, 18];
MediaMovil(p1,5)