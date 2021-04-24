A = float(input("digite valor de A:"))
B = float(input("digite valor de B:"))
C = float(input("digite valor de C:"))

if A > B  and B >= C :
    print(C, B, A)
    print("diferença entre é:", A - C)
elif B >= A and B > C and A >= C :
    print(C, A, B)
    print("diferença entre é:", B - C)
elif B > A and  B >= C and A <= C :
    print(A, C, B)
    print("diferença entre é:", B - A)
elif B > A and B <= C :
    print(A, B, C)
    print("diferença entre é:", C - A)
elif B > C and A < C :
    print(B, A, C)
    print("diferença entre é:", C - B)
elif B < C and C <= A :
    print(B, C, A)
    print("diferença entre é:", B - A)
else :
    print(A, B, C)
    print("diferença entre é:", C - A)


