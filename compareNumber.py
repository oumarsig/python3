print("Ce script recherche le plus grand de trois nombres")
print("Veuillez entrer trois nombres séparés par des virgules: ")
ch = input()
nn = list(eval(ch))
max, index = nn[0], "premier"
if nn[1] > max :
	max = nn[1]
	index = "deuxième"
if nn[2] > max :
	max = nn[2]
	index = "troisième"
print("Le plus grand de ces nombres est :", max)
print("Ce nombre est le ", index, "de votre liste de nombres.")
