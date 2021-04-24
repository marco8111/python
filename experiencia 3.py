res = 0
print('insira 1 digito :')
d = eval(input('insira (-1) para terminar programa/n'))
while d != -1 :
    res = res * 10 + d
    print('insira 1 digito :')
    d = eval(input('insira (-1) para terminar programa/n'))
print(res)    
