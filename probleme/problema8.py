def binar(x):
    """
    functie de conversie din zecimal in binar
    :param x: nr de convertit
    :return: nr x in binar
    """
    x1 = [0]*x
    i = 0
    while x > 0:
        x1[i] = x % 2
        x = int(x/2)
        i+=1

    nr = 0
    for j in range(i - 1, -1, -1):
        nr = nr*10 + x1[j]

    return nr


def problema8(n):
    binare = []
    """
    numerele binare intre 1 si n
    :param n: numar natural
    :return: numerele binare intre 1 si n
    """
    for i in range(1, n+1):
        binare.append(binar(i))

    return binare

assert(problema8(5)==[1, 10, 11, 100, 101])
assert(problema8(4)==[1, 10, 11, 100])