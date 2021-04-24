lst = [2, 5, 10, 100, 200, 300]
el = int(input('insira o numero a comparar'))
def parte(lst, el) :
    i = 0
    maior = []
    
    menor = []
    for i in lst:
        if el < i :
            maior = maior + [i]
        else :
            menor = menor + [i]
     
    return [menor, maior]
print(parte(lst, el))
