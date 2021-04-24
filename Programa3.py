

res = 0
print("escreve 1 digito")
val = eval(input("(-1 para terminar)\n? "))

while val != -1 :
    res = res * 10 + val
    print("escreva um digito")
    val = eval(input("(-1 para terminar)\ n? "))
print("o numero é :", res)
