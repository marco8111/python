

frase = input("insira frase:")
cont = 0
cont2 = 0
for i in frase :
    if(i.isdigit()) :
        cont += 1
    if(i.isidentifier()) :
        cont2 += 1
print("o numero de algarismo é:", cont)
  
print("o numero de letras é" ,cont2)      
