
def parte(lst, e) :
    menores = []
    maiores = []
    
    for i in lst:
        if i < e:
            menores = menores + [i]
        else :
            maiores = maiores + [i]
    return [menores, maiores]

r = parte([2, 0, 12, 19, 5], 6)
print(r)        
