# Réalisez un algorithme permettant de rechercher une valeur dans un tableau. 
# Si la valeur se trouve bien dans la tableau, nous affichons sa position.

# Imports
from random import randint

# Déclaration & Initialisation
array = ['Bonjour', 3, True, "Alain", "Quentin", 3, 3.25]
found_indexes = []
LENGTH = 10

# Remplissage du tableau
# for i in range(LENGTH):
#   array.append(randint(1, 100))

print(array)

# Demander à l'utilisateur d'entrer une valeur à rechercher dans le tableau
search_value = input("Entrez une valeur à rechercher : ")

# Recherche dans le tableau
for i, v in enumerate(array):
  if search_value == str(v):
    found_indexes.append(i)

# Affichage des résultats
if len(found_indexes) > 0:
  print(f"La valeur {search_value} a été trouvée", end=" ")
  if len(found_indexes) > 1: print("aux indices :", found_indexes)
  else: print("à l'indice :", found_indexes[0])
else:
  print(f"Aucune valeur trouvée dans le tableau pour la valeur {search_value}")
