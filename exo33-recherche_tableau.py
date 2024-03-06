tab = [1, 2, 3, 4, 5]
taille = len(tab)
nb = int(input("Quelle valeur il faut rechercher ?"))


def recherche_tableau(tableau, taille, nombre):
    position = -1
    i = 0
    while i < taille:
        if tableau[i] == nombre:
            position = i
        i += 1
    return position


print(recherche_tableau(tab, taille, nb))
