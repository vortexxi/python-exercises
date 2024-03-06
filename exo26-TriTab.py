# À l’aide des boucles, réalisez un algorithme permettant 
# de trier un tableau d’entier dans l’ordre croissant

array = [5, 1, 7, 9, 1, 3, 4]

# 1ere façon

for i in range(0, len(array) - 1):
  for j in range(i + 1, len(array)):

    if array[i] > array[j]:
      array[i], array[j] = array[j], array[i]


print(array)
