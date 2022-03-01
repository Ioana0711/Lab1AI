from sortari.merge_sort import merge_sort


def problema4(sir):
    """
    functia formeaza o lista cu toate cuvintele din sir
    ordonez crescator dpdv alfabetic lista
    apoi caut cuvintele unice din lista si returnez
    lista de cuvinte unice
    :param sir: fraza initiala
    :return: o lista care contine cuvintele unice din lista
    """
    cuvinte = sir.split(" ")
    unice=[]
    merge_sort(cuvinte)
    for i in range(len(cuvinte)):
        count = 0
        for j in range(len(cuvinte)):
            if cuvinte[i] == cuvinte[j]:
                count+=1
        if count == 1:
            unice.append(cuvinte[i])
    return unice

assert(problema4("ana are ana are mere rosii ana verzi rosi")==['mere', 'rosi', 'rosii', 'verzi'])
assert(problema4("ana are ana are mere rosii ana")==['mere', 'rosii'])