# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:20:36 2020

@author: Mult9
"""


listaalunos = []
na = int(input("insira num alunos da turma:"))
i = 0
for i in range(na) :
    nome = input("insira nome do aluno :")
    listaalunos.append(nome)
    
    

print(listaalunos)
f = 0
for f in range(len(listaalunos)) :
    listaalunos.sort()
    print("=============lista alunos============")
    print("Aluno" ,f + 1 ,listaalunos[f])
    
    
