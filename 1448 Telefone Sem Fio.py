from sys import stdin
stdin.reconfigure(encoding='latin-1')

while True:
    entrada = int(input())
    for caso in range(1, entrada + 1):
        frase = input()
        a = input()
        b = input()

        print("Instancia %d" % caso)
        if a == b:  # caso base: iguais
            print("empate\n")
            continue

        contA = 0
        contB = 0

        erA = -1  # aux
        erB = -1

        N = len(frase)

        for i in range(0, N):
            if a[i] != frase[i]:
                contA += 1
                if erA == -1:
                    erA = i
            if b[i] != frase[i]:
                contB += 1
                if erB == -1:
                    erB = i
            if erA == erB:
                erA = -1
                erB = -1

        if contA == contB and erB == erA:
            print("empate\n")
            continue

        if contA < contB:
            print("time 1\n")
        elif contA > contB:
            print("time 2\n")

        else:
            if erA > erB:
                print("time 1\n")
            else:
                print("time 2\n")
