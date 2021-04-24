n = eval(input("insira um numero:"))


def explode(n) :
    if isinstance(n, int) :
        res = ()
        while n!= 0 :
            res = (n%10,) + res
            n = n // 10
            
        return res
        
    else:
        print("valueError: {} :argumento nao inteiro ".format(n))

print(explode(n))    
