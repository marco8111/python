a = int(input('insira num:'))
b = int(input('insira num:'))
c = int(input('insira num:'))
if a > b and b >c :
    print(a, b, c)
    print('o maior numero é {}'.format(a))
elif b > a and a > c :
    print(a, b, c)
    print('o maior numero é {}'.format(b))
else :
    print(a, b, c)
    print('o maior numero é {}'.format(c))
