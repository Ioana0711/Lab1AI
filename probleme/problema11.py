import numpy


def problema11(matrix):
    replaceSurrounded(matrix)
    return numpy.array(matrix)


# Functie recursiva care inlocuieste
# prevV de la pozitia (x,y) si din jurul acestei valori
# cu noua valoare newV

def floodFillUtil(matrice_noua, x, y, prevV, newV):
    # Conditii de oprire
    if x < 0 or x >= len(matrice_noua) or y < 0 or y >= len(matrice_noua[0]):
        return

    if matrice_noua[x][y] != prevV:
        return
    # Inlocuim valoarea unui element al matricei cu noua valoare
    matrice_noua[x][y] = newV

    # Apel recursiv pentru toate cazurile
    floodFillUtil(matrice_noua, x + 1, y, prevV, newV)
    floodFillUtil(matrice_noua, x - 1, y, prevV, newV)
    floodFillUtil(matrice_noua, x, y + 1, prevV, newV)
    floodFillUtil(matrice_noua, x, y - 1, prevV, newV)


# Returneaza matricea modificata
def replaceSurrounded(matrice_noua):
    # Step 1: Replace all 'O's with '-'
    for i in range(len(matrice_noua)):
        for j in range(len(matrice_noua[0])):
            if matrice_noua[i][j] == 0:
                matrice_noua[i][j] = -1

    # Apelam functia floodFillUtil pentru toate
    # valorile de -1 de pe marginile matricei
    # unde nu este respectata conditia
    # inlocuim acele valori de -1 cu 0

    # Partea stanga a matricei
    for i in range(len(matrice_noua)):
        if matrice_noua[i][0] == -1:
            print('ok')
            floodFillUtil(matrice_noua, i, 0, -1, 0)

    # Partea dreapta a matricei
    for i in range(len(matrice_noua)):
        if matrice_noua[i][len(matrice_noua[0]) - 1] == -1:
            floodFillUtil(matrice_noua, i, len(matrice_noua[0]) - 1, -1, 0)

    # Partea superioara a matricei
    for i in range(len(matrice_noua[0])):
        if matrice_noua[0][i] == -1:
            floodFillUtil(matrice_noua, 0, i, -1, 0)

    # Partea inferioara a matricei
    for i in range(len(matrice_noua[0])):
        if matrice_noua[len(matrice_noua) - 1][i] == -1:
            floodFillUtil(matrice_noua, len(matrice_noua) - 1, i, -1, 0)

    # 3: Inlocuim -1 cu 1
    for i in range(len(matrice_noua)):
        for j in range(len(matrice_noua[0])):
            if matrice_noua[i][j] == -1:
                matrice_noua[i][j] = 1

    return matrice_noua
