mes = int(input("digite o mes:"))
if ((mes <= 0) or (mes > 12)) :
    print("mes invalido")
else :
    ano = int(input("insira valor de anos:"))
if (ano % 4 == 0) and (ano % 100 != 0) :
    print("ano bissexto")
elif (ano % 400 == 0) :
    print("ano bissexto")
else :
    print("ano comun")
