seau = 0
capacite_seau = 17
marmite = 0


def remplir_seau():
    patates = 0
    for i in range(capacite_seau):
        patates += 1
    return patates


def retirer_patate(seau):
    patate = 1
    seau -= patate
    return seau


def ajouter_patate(marmite):
    patate = 1
    marmite += patate
    return marmite


def show_info(marmite, seau):
    print("#"*20)
    print(f"Il y a {marmite} patates dans la marmite.")
    print(f"Il y a {seau} patates dans la seau.")
    print("#"*20)


while marmite < 50:
    if seau > 0:
        seau = retirer_patate(seau)
        marmite = ajouter_patate(marmite)
    else:
        seau = remplir_seau()
    show_info(marmite, seau)
