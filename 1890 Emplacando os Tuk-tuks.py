#26 consoantes e 10 digitos
t = int(input())
while t:
    t -= 1 #ate chegar a 0
    c, d = [int(x) for x in input().split()] #percorrer a lista de c, d
    placas = (26**c) * (10**d) #calculo de combinação
    if placas == 1:
        placas = 0
    print(placas)