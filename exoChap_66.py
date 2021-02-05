cn = range(0, 32)
res = 0
for a in cn:
	if a % 3==0 or a % 5==0:  #and 
		res = res + a
print(res)
print("Donnez une année de votre choix:")
année = input()
an = int(année)
if an:
	if an % 4 ==0:
		print("L'année", an ," est bissextile")
	elif an % 100 == 0 and an % 400 !=0:
		print("L'année", an ," n'est pas bissextile")
else:
	print("Donnez une année de votre choix:")

