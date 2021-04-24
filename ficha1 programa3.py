res = 0
print('insira 1 num')
print('-1 para terminar programa/n!!!!')
n = eval(input('insira 1 digito :'))
while n != -1 :
    res = res * 10 + n
    print('-1 para terminar programa/n!!!!')
    n = eval(input('insira 1 digito'))
print('o numeros resultante e :', res)    
