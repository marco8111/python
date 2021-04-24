

dia = int(input("Insira dia nascimento:"))
mes = int(input("Insira Mes de nascimento:"))
ano = int(input("insira ano de nascimento:"))

if ano > 2020 :
    print("Ano Invalido")
else :
    print("data atual : 25/novembro/2019")
ano = 2019 - ano
mes = 11 - mes
dia = 28 - dia
print("A sua idade é :"  +str(ano)+ "anos" +str(mes)+ "meses" +str(dia)+ "dias")


