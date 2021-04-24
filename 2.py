col = int(input("a coluna de 3 elementos:"))
lin = int(input("a linha de 3 elementos:"))
lista = []
lista1 = []
i = 0
x = 0
c = 0
while i != col:
    while x != lin:
        ele = input("insira o elemento")
        lista.append(ele)
        x += 1
    x = 0
    lista1 += [lista]
    lista = []
    i += 1
print("Matriz original: ")
while c != col:
    print(lista1[c])
    c += 1