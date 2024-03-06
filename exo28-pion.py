# Réalisez un algorithme nous permettant de déplacer un 
# pion dans un tableau de 10 éléments. 
# Au début, le pion se trouve dans la première case du tableau. 
# Nous pouvons ensuite le déplacer par la gauche (g), 
# par la droite (d) ou de stopper l'algorithme (q) 
# (Indice : l'exo doit être exécuté dans la console Windows). 

# Imports
import msvcrt as m
from os import system

# Déclaration et initialisation
tab = [" "] * 10
index = 8
tab[index] = "X"

# Affichage du tableau
print(tab)

key = m.getch()
char = key.decode("ascii")

# print(key)
# print(char)

while char != "w":

  if char == "d":
    # Droite
    if index < len(tab) - 1:
      tab[index + 1], tab[index] = tab[index], tab[index + 1] 
      index += 1
    else: 
      # print("Vous ne pouvez pas aller plus loin.")
      tab[0], tab[index] = tab[index], tab[0] 
      index = 0

  if char == "q":
    # Gauche
    if index > 0:
      tab[index - 1], tab[index] = tab[index], tab[index - 1] 
      index -= 1
    else: 
      # print("Vous ne pouvez pas aller plus loin.")
      tab[len(tab) - 1], tab[index] = tab[index], tab[len(tab) - 1] 
      index = len(tab) - 1

  system("cls")
  print(tab)
  key = m.getch()
  char = key.decode("ascii")