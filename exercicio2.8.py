fim = int(input("digite o valor de fim:"))
ini = int(input("digite o valor de ini:"))
if ini < 1 :
    print("numero não é valido")
elif fim <= ini :
    print("intervalo invalido")
Y = 0
num = ini
while num <= fim :
    for i in range(1,num + 1) :
        if num % i == 0 :
            Y = Y+ 1

    if Y == 2 :
        print(num)
    num = num + 1
    Y= 0
