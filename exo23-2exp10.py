# BONUS : initialiser un tableau de 10 entiers avec les valeurs
# 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 à l’aide d’une boucle.
# Ensuite, à l’aide d’une boucle afficher la valeur de chaque cellule
# du tableau avec l’opération Ecrire().

tab = []
MAX_VALUE = 10

# Initialisation du tableau
for i in range(MAX_VALUE):
  tab.append(2 ** (i + 1)) # ** = Exposant

# Affichage du tableau
for number in tab:
  print(number)

