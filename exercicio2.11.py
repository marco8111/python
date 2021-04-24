largurac = int(input("insira largura do contentor:"))
comprimentoc = int(input("insira comprimento do contentor:"))
alturac = int(input("insira altura do contentor:"))

larguran = int(input("insira largura do navio:"))
comprimenton = int(input("insira comprimento do navio:"))
alturan = int(input("insira altura do navio:"))

quantx = int(larguran / largurac)
quanty = int(comprimenton / comprimentoc)
quantz = int(alturan / alturac)

print (int(quantx * quanty * quantz))
