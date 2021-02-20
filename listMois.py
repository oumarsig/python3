t1=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2=["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]
t3=[]
for i in range(len(t1)):
    t3.append(t2[i])
    t3.append(t1[i])
print(t3)

for mois in t2:
    print(mois)

t4 = [32, 5, 12, 8, 3, 75, 2, 15]
### maxi = t4[0]
pairs = []
impairs = []
maxi = 0
for numb in t4:
    if numb>maxi:
        maxi=numb
print(maxi)

for numb in t4:
    if numb % 2 == 0:
        pairs.append(numb)
    else:
        impairs.append(numb)
print("pairs = ", pairs)
print("impairs = ", impairs)

t5 = ["Serigne Saliou Niang", "Oumar Niang", "Nafissatou", "Momar", "Djamal", "Mbade", "Pithie"]
nameShort = []
nameLong = []
for name in t5:
    if len(name) < 6:
        nameShort.append(name)
    else:
        nameLong.append(name)
print("Noms Courts =  ", nameShort)
print("Noms Longs = ", nameLong)
