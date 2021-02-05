print("Choisissez un nombre de 1 à 3 ( ou 0 pour terminer)", end=" ")
ch = input()
a = int(ch)
while a: 
	if a == 1:
		print("Vous avez choisi un:")
		print("le premier, l'unique, l'unité...")
	elif a == 2:
		print("Vous avez choisi le deux:")
		print("la paire, le couple, le duo....")
	elif a == 3:
		print("Vous optez pour le plus grand")
		print("le trio, le triplet, la troisième femme....")
	else:
		print("Un nombre entre Un et Trois, please!")
	print("Choisissez un nombre de 1 à 3 ( ou 0 pour terminer)", end="")
	a = int(input(ch))
print("Vous avez entré zéro:")
print("L'exercice est donc terminé")

