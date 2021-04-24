# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:54:42 2020

@author: Mult9
"""

lista =[]
lista.append(eval(input("insira 1 numr:")))
lista.append(eval(input("insira 1 numr:")))
lista.append(eval(input("insira 1 numr:")))
print(lista)
el = eval(input("insira elemento:"))

def posicoeslista(lista, el) :
    res = []
    i = 0    
    for i in range(len(lista)) :
        if el == lista[i] :    
            res = res + [i]         
    return res
print(posicoeslista(lista, el))
                    
    
    

    
    