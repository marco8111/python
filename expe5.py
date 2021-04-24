lst = [2, 4, 5,  5, 4, 3, 7, 8]
def remove_repetidos(lst) :
    novalst = []
    for i in lst :
        if i not in novalst :
            novalst = novalst + [i]
    return novalst
print(remove_repetidos(lst))
            
