nb1 = int(input("Entrez le nombre 1 : "))
op = input("Entrez l'opérateur : +, -, *, / : ")
nb2 = int(input("Entrez le nombre 2 : "))

if op == "+":
	print(nb1, op, nb2, "=", nb1+nb2)
elif op == "-":
	print(nb1, op, nb2, "=", nb1-nb2)
elif op == "*":
	print(nb1, op, nb2, "=", nb1*nb2)
elif op == "/":
	if nb2 == 0:
		print("Division par 0")
	else :
		print(nb1, op, nb2, "=", nb1+nb2)
else :
	print("Opérateur inconnu")
input("Appuyez sur Enter")