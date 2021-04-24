# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:06:18 2020

@author: Marco Silva
"""

n = int(input("insira n:"))
if (n <= 0) :
    print("numero invalido")
else :
    x = 1
    soma = 0
    while  x < n :
       soma = x + soma
       x += 1
       print(soma)
        
    



