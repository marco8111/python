num = print(int(input("insira 1 numero de 3 digitos:")))
ex100 = num // 100
print(ex100)
if ex100 >= 1 and ex100 < 10 :
    ex10 = (num - (ex100) * 100) / 10

    ex1 = int((ex10 * 10) - (int(ex10) * 10)

    ex10 = int((num - (ex100) * 100) * 10)

    print(str(num)+" = "+str(ex1)+" * 1 +"+str(ex10)+ " * 10 +"+str(ex100)+" * 100 ")
else :
    print("o numero nao tem 3 digitos:")


