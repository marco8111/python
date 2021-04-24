lst = [2, 'a', 'c', 2, 4]
el = input('insira o que que procurar :')

def posicao_lista(lst, el) :
    lst1 = []
    i = 0
    while i < len(lst):
        if el == lst[i] :
            lst1.append(lst[i])
        else :    
            i += 1
    return lst1
print(posicao_lista(lst, el))
        
