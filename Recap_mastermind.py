# Importer OS
import os

# Créer la combinaison
from random import choice

couleur1 = choice(["rouge", "bleu", "jaune", "vert", "mauve", "orange"])
couleur2 = choice(["rouge", "bleu", "jaune", "vert", "mauve", "orange"])
couleur3 = choice(["rouge", "bleu", "jaune", "vert", "mauve", "orange"])
couleur4 = choice(["rouge", "bleu", "jaune", "vert", "mauve", "orange"])
combinaison = [couleur1, couleur2, couleur3, couleur4]

# Afficher le choix
def afficher_choix():
    print("r : rouge")
    print("b : bleu")
    print("j : jaune")
    print("v : vert")
    print("m : mauve")
    print("o : orange")

# Vérifier les choix proposés
choix_possible = ["r", "b", "j", "v", "m", "o"]

# Demander les choix
def demander_choix(numero):
    os.system('cls')
    print(f"Donner un couleur pour l'emplacement n°{numero} parmis les couleurs suivantes :")
    afficher_choix()
    choix = input(">>>  ")
    return choix

# Fonction qui change les lettres de la proposition en correct mot
def transformer_proposition():
    for i, letter in enumerate(proposition):
        if letter == "r":
            proposition[i] = "rouge"
        elif letter == "b":
            proposition[i] = "bleu"
        elif letter == "j":
            proposition[i] = "jaune"
        elif letter == "v":
            proposition[i] = "vert"
        elif letter == "m":
            proposition[i] = "mauve"
        elif letter == "o":
            proposition[i] = "orange"

# Afficher le résultat
def afficher_resultat():
    os.system('cls')
    print(f"Combinaison : {combinaison}")
    print(f"Proposition : {proposition}")
    print(f"Bonne endroit : {bon_endroit} | Mauvais endroit : {mauvais_endroit}")
    print(f"Nombre de tentative restante : {10-tentative}")
    print("\n"*5)
    input("Appuyer sur ENTER pour continuer")

# Initialiser le nombre de tentative et la liste des propositions
tentative = 1
proposition = []

# Afficher message de bienvenue
print("Bienvenue dans MasterMind !\nEssayer de deviner la bonne combinaison de 4 couleurs.")

# Lancer la partie
while proposition != combinaison and tentative <= 10:
    proposition_valide = False
    while proposition_valide != True:
        proposition.clear()
        choix1 = demander_choix(1)
        choix2 = demander_choix(2)
        choix3 = demander_choix(3)
        choix4 = demander_choix(4)

        # Ajouter les choix dans la liste de proposition
        proposition.extend([choix1, choix2, choix3, choix4])

        # Vérifier les propositions
        bad_proposition = 0
        for choix in proposition:
            if choix not in choix_possible:
                bad_proposition += 1
                print(f"Désolé. Le choix {choix} n'est pas valide !")
                print("Veillez recommencer")
                input("Appuyer sur ENTER pour continuer.")
        if bad_proposition == 0:
            proposition_valide = True

    # Transformer les lettres de la proposition en mots
    transformer_proposition()

    # Vérifier le proposition
    bon_endroit = 0
    mauvais_endroit = 0

    combinaison_copy = combinaison[:]
    for i in range(4):
        if proposition[i] == combinaison_copy[i]:
            bon_endroit += 1
            combinaison_copy[i] = "x"
    for i in range(4):
        if proposition[i] in combinaison_copy:
            mauvais_endroit += 1
    
    # Résultat final
    os.system('cls')
    if proposition == combinaison:
        print(f"Félicitation pouvez cracker le Mastermind en seulement {tentative}!")
        print(f"Combinaison : {combinaison}")
    elif tentative == 10:
        print("Oh non. Vous avez échoué !")
        print(f"Votre dernière proposition : {proposition}")
        print(f"La bonne combinaison : {combinaison}")
    else:
        afficher_resultat()
    
    # Gérer les itérations
    proposition.clear()
    tentative += 1