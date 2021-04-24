res = 0
print('insira 1 numero :')
d =eval(input('insira -1 para encerrar programa :'))
while d != -1 :
    res = res * 10 + d
    print('insira 1 numero :')
    d = eval(input('insira -1 para terminar programa :'))
print(res)    
