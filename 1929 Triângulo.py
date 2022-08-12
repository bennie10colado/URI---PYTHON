i = input()
i = i.split(' ')

a = int(i[0])
b = int(i[1])
c = int(i[2])
d = int(i[3])
# um de seus lados deve ser maior que o mod da diferença dos outros dois lados( E AS DUAS DIFERENÇAS) e menor que a soma dos outros dois lados e
if a > c - b and a < b + c and a + c > b:
    print('S')
elif b > d - c and b < c + d and b + d > c:
    print('S')
elif a > d - c and a < c + d and a + d > c:
    print('S')
elif a > d - b and a < b + d and a + d > b:
    print('S')
else:
    print('N')