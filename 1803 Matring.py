#  (4932*1993 + 5479) mod 257 = 79 = O
#  matriz = []
#  matriz.append(" ")
#  pegar numeros inteiros por linha e usa-los

matriz1 = []

for i in range(4):
    linha = input()
    matriz1.append(linha)

matriz2 = []
aux = 0

for j in range(len(matriz1[0])):  #  matriz1[0] é o num de colunas
    aux = int(matriz1[0][j]) * 1000
    aux += int(matriz1[1][j]) * 100
    aux += int(matriz1[2][j]) * 10
    aux += int(matriz1[3][j])

    matriz2.append(aux)
#print(matriz2)

for k in range(1, len(matriz2)-1):  #  ignora primeira e ultima coluna
    #  print(k)
#  print(k)
    r = (matriz2[0] * matriz2[k] + matriz2[-1]) % 257
    print(chr(r), end = '')
print()
