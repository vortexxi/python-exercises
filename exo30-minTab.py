# Refaites l'algorithme qui demande à l’utilisateur de taper 10 entiers
# et qui affiche le plus petit de ces entiers mais cette fois-ci à l'aide
# d'un tableau et sans retenir le minimum lors de la saisie.

# Import
from random import randint

# Variables
array = []
length = 10


# Demander à l'utilisateur de rentrer 10 entiers dans un tableau
for i in range(length):
  # array.append(int(input(f"Entrez l'entier n°{i + 1} : ")))
  array.append(randint(1, 100))

min = array[0]
max = array[0]

# Rechercher la valeur minimum des entiers
for i, v in enumerate(array):
  if v  < min:
    min = v
  
  if v > max:
    max = v

# Affichage du résultat
print(array)
print(f"La valeur minimum est {min}")
print(f"La valeur maximum est {max}")
