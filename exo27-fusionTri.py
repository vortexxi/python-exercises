# En considérant deux tableaux d'entiers (non triés), 
# réalisez un algorithme qui place tous les éléments des deux 
# tableaux dans un troisième. 
# Ce dernier doit être trié une fois l'algorithme terminé. 
# Notez que le tri doit être fait en même temps que la fusion 
# des deux tableaux et pas après.

t1 = [8, 1, 5, 7, 1, 3]
t2 = [9, 4, 2, 6, 1, 3]
t3 = []

# Parcourir t1 et insérer au bon endroit dans t3
i = 0
while i < len(t1):
  saved_index = 0
  for index, value in enumerate(t3):
    if t1[i] > value:
      saved_index = index + 1
    else: break
  
  t3.insert(saved_index, t1[i])

  i += 1

# Parcourir t2 et insérer au bon endroit dans t3
i = 0
while i < len(t2):
  saved_index = 0
  for index, value in enumerate(t3):
    if t2[i] > value:
      saved_index = index + 1
    else: break
  
  t3.insert(saved_index, t2[i])

  i += 1


# Affichage des tableaux

print("Tableau 1 : ", t1)
print("Tableau 2 : ", t2)
print("Tableau 3 : ", t3)