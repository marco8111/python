A = int(input("digite Votos validos de A:"))
B = int(input("digite Votos validos de B:"))
C = int(input("digite Votos validos de C:"))

nda = int(input("digite Votos nulos de A:"))
ndb = int(input("digite Votos nulos de B:"))
ndc = int(input("digite Votos nulos de C:"))

eba = int(input("digite Votos em branco de A:"))
ebb = int(input("digite Votos em branco de B:"))
ebc = int(input("digite Votos em branco de C:"))

vnva = int(input("digite Votos não validos de A:"))
vnvb = int(input("digite Votos não validos de B:"))
vnvc = int(input("digite Votos não validos de C:"))

totaleleitores = (A + B + C + nda + ndb + ndc + eba + ebc)

percentual = float((A + B + C) * 100 / totaleleitores)
percentA = float((A * 100) / totaleleitores)
percentB = float((B * 100) / totaleleitores)
percentC = float((C * 100) / totaleleitores)
percentnul = float((vnva + vnvb + vnvc) * 100 / totaleleitores)
percenteB = float((eba + ebb + ebc) * 100 / totaleleitores)

print("Percentagem de eleitores é:", percentual)
print("Percentagem de votos em A:", percentA)
print("Percentagem de votos em B:", percentB)
print("Percentagem de votos em C:", percentC)
print("Percentagem de votos nulos :", percentnul)
print("Percentagem de votos em Branco:", percenteB)
