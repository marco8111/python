
lst = []
lst.append(eval(input("insira 1 numero:")))
lst.append(eval(input("insira 1 numero:")))
lst.append(eval(input("insira 1 numero:")))
lst.append(eval(input("insira 1 numero:")))
lst.append(eval(input("insira 1 numero:")))
lst.append(eval(input("insira 1 numero:")))
e = eval(input("insira 1 elmento a comparar:"))



def parte(lst, e) :
    menores = []
    maiores = []
    
    for i in lst:
        if i < e:
            menores= menores + [i]
        else :
            maiores = maiores + [i]
    return [menores, maiores]

r = parte(lst, e)
print(r)        
