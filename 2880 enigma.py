cifra = str(input())
frase = str(input())

contador = 0
erro = 0

for i in range(len(cifra) - len(frase) + 1):

    for j in range(len(frase)):

        if cifra[i + j] == frase[j]:  # condicao de existencia de uma frase no enigma, se forem de tamanhos iguais, entao é um erro
            break

        else:  # senao vai contar um erro
            erro += 1

    if erro == len(frase):
        contador += 1 #contagem de erros
    erro = 0

print(contador)