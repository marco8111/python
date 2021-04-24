

el = int(input('insira o num :'))
lst = [2, 3, 4]

def pertence(el, lst):
    i = 0
    while i < len(lst):
        if el == lst[i]:
            return True
        i += 1
    return False
 
print(pertence(el, lst))        
    
    
    
    
    
   
    

