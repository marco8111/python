lst = [2, 'a', 'a', 'c', 2, 3]
el = eval(input('insira elemento :'))
def posicaolista(lst, el) :
    res = []
    i = 0
    for i in range(len(lst)) :
        if el == lst[i] :
            res = res + [i]
    return res
print(posicaolista(lst, el))
