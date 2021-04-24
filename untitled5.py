# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:05:18 2020

@author: Marco Silva
"""

def bissexto() :
    ano = int(input("insira o ano :"))
    if (ano % 4 == 0) :
        return True
    elif (ano % 100 == 0):
        return True
    else :
        return False

print(bissexto())
