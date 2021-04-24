# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:11:19 2020

@author: Mult9
"""


salariohr = float(input("insira salario por hr:"))
hrst = float(input("insira horas de trabalho:"))

def paus(salariohr, hrst) :
    salario = 0    
    salario = salariohr * hrst
    return(salario)
print("Vc trabalhou", hrst, "e recebe", paus(salariohr, hrst))