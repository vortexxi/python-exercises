# Écrire un algorithme demandant à l’utilisateur le nombre de joueurs (max 10 joueurs). 
# Ensuite, l’algorithme doit demander à l’utilisateur le score de chaque joueur. 
# Une fois ceci fini, il faut afficher la moyenne des scores.

# Déclaration / Initialisation
scores = []
MAX_PLAYERS = 10
nb_players = 0

# Demander à l'utilisateur de rentrer le nombre de joueurs
while not 1 <= nb_players <= MAX_PLAYERS:
  nb_players = int(input("Entrez le nombre de joueurs de votre équipe (max: 10 joueurs): "))

# Demander à l'utilisateur le score de chaque joueur et calculer la somme
sum = 0
for i in range(nb_players):
  score = int(input(f"Entrez le score du joueur n°{i + 1} : "))
  sum += score
  scores.append(score)

# Calculer la moyenne des scores
average = sum / nb_players

# Affichage de la moyenne des scores
print(f"La moyenne des scores est de {average} pour les scores {scores}.")
print(f"La moyenne des scores est de {round(average, 2)} pour les scores {scores}.")