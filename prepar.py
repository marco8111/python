n = eval(input('insira 1 num:'))
n1 = eval(input('insira outro num:'))
x = eval(input('qual operacao 1-soma, 2-sub, 3-mult, 4-div:'))
z = 0
if x == 1 :
   z = n + n1
   print(z)
elif x == 2 :
    z = n - n1
    print(z)
elif x == 3 :
    z = n * n1
    print(z)
elif x == 4 :
    z = n / n1
    print(z)
