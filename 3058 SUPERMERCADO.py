menor_valor = []

n = int(input())

for i in range(n):
    p,g = map(float, input().split(" "))
    preco_grama = (p*1000) / g
    menor_valor.append(preco_grama)

print(f'{min(menor_valor):.2f}')