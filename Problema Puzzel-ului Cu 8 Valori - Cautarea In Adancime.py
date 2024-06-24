# Rezolvarea puzzel-ului cu 8 valori folosind algoritmul de căutare în adâncime
def este_rezolvabil(stare):
    inversiuni = 0
    stare_liniarizata = [valoare for rand in stare for valoare in rand if valoare != 0]
    for i in range(len(stare_liniarizata)):
        for j in range(i + 1, len(stare_liniarizata)):
            if stare_liniarizata[i] > stare_liniarizata[j]:
                inversiuni += 1
    return inversiuni % 2 == 0


def pozitie_0(stare):
    for i in range(3):
        for j in range(3):
            if stare[i][j] == 0:
                return i, j


def actiuni(stare):
    pozitie_0_i, pozitie_0_j = pozitie_0(stare)
    actiuni_posibile = []

    if pozitie_0_i > 0:
        actiuni_posibile.append("Sus")
    if pozitie_0_i < 2:
        actiuni_posibile.append("Jos")
    if pozitie_0_j > 0:
        actiuni_posibile.append("Stanga")
    if pozitie_0_j < 2:
        actiuni_posibile.append("Dreapta")
    return actiuni_posibile


def aplicare_actiuni(stare, actiune):
    pozitie_0_i, pozitie_0_j = pozitie_0(stare)
    i, j = pozitie_0_i, pozitie_0_j

    if actiune == "Sus":
        i -= 1
    elif actiune == "Jos":
        i += 1
    elif actiune == "Stanga":
        j -= 1
    elif actiune == "Dreapta":
        j += 1

    stare_noua = [rand[:] for rand in stare]
    stare_noua[pozitie_0_i][pozitie_0_j], stare_noua[i][j] = \
        stare_noua[i][j], stare_noua[pozitie_0_i][pozitie_0_j]
    return stare_noua


def cautare(stare_initiala):
    if not este_rezolvabil(stare_initiala):
        print("Starea dată nu este rezolvabilă!\n")
        return None

    noduri_de_explorat = [(stare_initiala, None, None)]
    noduri_deja_explorate = set()

    while noduri_de_explorat:
        nod = noduri_de_explorat.pop(0)
        stare, starea_precendenta, actiune = nod
        if stare == stare_finala:
            return stare, starea_precendenta
        noduri_deja_explorate.add(str(stare))

        for actiune in actiuni(stare):
            starea_urmatoare = aplicare_actiuni(stare, actiune)
            if str(starea_urmatoare) not in noduri_deja_explorate:
                noduri_de_explorat.append((starea_urmatoare, nod, actiune))
    return None


def afiseaza_stare(stare):
    for rand in stare:
        print(rand)
    print()


def afiseaza_cale(nod):
    cale = []
    while nod is not None:
        cale.append(nod[0])
        nod = nod[1]
    cale.reverse()
    for index, stare in enumerate(cale):
        print(f"Pasul {index + 1}:")
        afiseaza_stare(stare)


stare_initiala = [[2, 3, 1], [6, 4, 5], [7, 8, 0]]
stare_finala = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

nod_rezultat = cautare(stare_initiala)
if nod_rezultat:
    print("Soluția a fost găsită!\n")
    afiseaza_cale(nod_rezultat)
else:
    print("Nu s-a găsit soluție!")
