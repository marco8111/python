A = int(input("Insira tamanho de lado A:"))
B = int(input("Insira tamanho de lado B:"))
C = int(input("Insira tamanho de lado c:"))

if (A <= B + C) and (B <= A + C) and (C <= A + B) :
    print("Estes Valores formam um triangulo")
else :
    print("estes valores nao formam um triangulo")

if A == B and B == C :
    print("triangulo equilatero")
elif A == B and C > B :

    print("Triangulo Isosceles")
if A != B and B != C and A != C :
    print("triangulo escaleno")
