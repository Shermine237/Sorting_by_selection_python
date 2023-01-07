# Algorithme tri par selection


def tri_selection(liste_unsorted):
    liste_sorted = []
    numb_and_index = [(numb, liste_unsorted.index(numb)) for numb in liste_unsorted]
    for number in numb_and_index:
        numb_min = number      # on considere que le 1er element est le plus petit, forme (numb, index)
        for numb in numb_and_index:
            if numb[0] < numb_min[0]:
                numb_min = numb
        liste_sorted.append(numb_min)

    print(liste_sorted)


liste = (8, 5, 4, 15, 4, 1, 15, 28, 3)
tri_selection(liste)
