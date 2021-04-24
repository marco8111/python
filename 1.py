dia = int(input("digite o valor do dia do mês de 1 a 31: "))
mes = int(input("digite o valor da mês para que março = 3, abril = 4,..., janeiro = 13, fevereiro = 14: "))
ano = int(input("digite o valor do ano: "))
semana = ["sabado","domingo","segunda","terça","quarta","quinta","sexta"]
def dia_da_semana(dia,mes,ano):
    res = []
    if dia >= 0 and dia <= 31 and mes >= 3 and mes <= 14 and ano > 0:
        k = ano % 100
        j = ano // 100
        h = int((dia + (13 * (mes + 1) / 5) + k + (k / 4) + (j / 4) - 2 * j) %7)
        print(dia, mes, ano)
        if h == 0:
            res = semana[0]
        if h == 1:
            res = semana[1]
        if h == 2:
            res = semana[2]
        if h == 3:
            res = semana[3]
        if h == 4:
            res = semana[4]
        if h == 5:
            res = semana[5]
        if h == 6:
            res = semana[6]
    else:
        print("tente de novo")
    return res
print(dia_da_semana(dia,mes,ano))