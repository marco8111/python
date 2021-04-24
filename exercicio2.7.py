x = int(input("digite o numero :"))

divisores = 0
for i in range(1, x+1) :
    if x % i == 0 :
        divisores = divisores + 1

if divisores == 2 :
    print("numero", x, "é primo")
else :
    print("numero não é primo:")
