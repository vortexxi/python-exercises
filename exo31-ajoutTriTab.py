# En considérant un tableau d'entiers trié dans l'ordre croissant, 
# réaliser un algorithme étant capable d'insérer une nouvelle valeur 
# dans le tableau de façon à ce que la tableau reste trié.
# Le but n'est évidemment pas d'insérer la valeur à la fin et de trier 
# après mais bien de l'insérer au bon endroit directement.

array = [0, 10, 20, 30, 40, 50]

value_to_insert = int(input("Entrez une valeur à insérer : "))

saved_index = 0
for index, value in enumerate(array):
  if value_to_insert > value:
    saved_index = index + 1
  else: break

array.insert(saved_index, value_to_insert)

print(array)
