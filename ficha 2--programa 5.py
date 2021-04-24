def remove_repetidos(lista) :
    l = []
    x = []
    for i in lista :
        if i not in l:
            l.append(i)
    return l
lista = [1, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10]
print(remove_repetidos(lista))
