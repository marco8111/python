# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:24:10 2020

@author: Marco Silva
"""
def filtra_pares(tn) :
    par = ()
    i = 0    
    for i in tn:
        if isinstance(i, int) and 0 <= i <= 9 :
            if i%2 == 0:
                par = (i,) + par
        else :
            raise ValueError("filtra pares: argumento nao inteiro")
    return par
tn = (1, 2, 2, 4, 6, 8 , 9, 6, 8 )
print(sorted(filtra_pares(tn)))   