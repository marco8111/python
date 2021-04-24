el = int(input('insira 1 elemento :'))

lst = [2, 3, 4]
def pertence(lst, el):
    i = 0
    while i < len(lst):
        if el == lst[i]:
            return True
        i += 1
    return False        
print(pertence(lst, el))

