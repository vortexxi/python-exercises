# Inverser un tableau : soit un tableau T. Saisir ce tableau. 
# Changer de place les éléments de ce tableau de façon à ce que 
# le nouveau tableau soit une sorte de miroir de l'ancien et 
# afficher le nouveau tableau.

# Première façon
array = [5, 4, 1, 9, 3, 2]

reversed_array = array[::-1]

print(array)
print(reversed_array)

# Deuxième façon
reversed_array = array[:]
reversed_array.reverse()

print(reversed_array)

# Troisième façon

reversed_array = []

for i in range(len(array) - 1, -1, -1):
  reversed_array.append(array[i])

print(reversed_array)
