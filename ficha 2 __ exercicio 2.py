# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:54:42 2020

@author: Mult9
"""

el = eval(input("insira 1 caractere:_"))
lst = [2, 'a', 'c', 2, 'a']
def posicoeslista(lst, el):
    i = 0 
    result = []   
    for i in range(len(lst)) :
        if el == lst[i] :
            result = result + [i]
    return result
print(posicoeslista(lst, el))
                 
    
    
