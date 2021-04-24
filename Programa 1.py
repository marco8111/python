# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:38:55 2020

@author: Marco Silva
"""

a = int(input("insira 1ro num:"))
b = int(input("insira 2ndo num:"))
c = int(input("insira 3ro num:"))


if (a > b) and (b > c) :
    print(a, ",", b, ",", c)
    print("o maior numero é:", a)

elif (b > a) and (a > c) :
    print(b, ",", a, ",", c)
    print("o maior numero é:", b)

elif (c > b) and (b > a) :
    print(c, ",", b, ",", a)
    print("o maior numero é:", c)

elif (b > c) and (c > a) :
    print(b, ",", c, ",", a)
    print("o maior numero é:", b)

elif (a > b) and (c > b) :
    print(a, ",", c, ",", b)
    print("o maior numero é:", a)
else :
    print(a, ",", b, ",", c)
    print("estes nmros sao iguais")
  
  
    
    