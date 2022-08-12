while True:
    largura, comp, r1, r2 = [int(x) for x in input().split()]  # cada linha é recebida através de um for

    if (largura == 0 and comp == 0 and r1 == 0 and r2 == 0):  # condicao de parada
        break

    diam1 = r1 * 2
    diam2 = r2 * 2
    lc = diam1 * 2  # espaço alocado por 2 diametros, logica de um circulo ocupar o espaço de um quadrado
    
    if largura > comp:
        if (largura >= lc) and ((comp >= diam1) or (comp >= diam1)):
            print('S')
        else:
            print('N')

    elif comp > largura:
        #print(comp, lc, largura, diam1, diam2)
        if (comp >= lc) and ((largura >= diam1) or (largura >= diam2)):
            print('S')
        else:
            print('N')

    else:
        if (largura >= lc) and ((comp >= diam1) or (comp >= diam2)):
            print('S')
        elif (comp >= lc) and ((largura >= diam1) or (largura >= diam2)):
            print('S')
        else:
            print('N')