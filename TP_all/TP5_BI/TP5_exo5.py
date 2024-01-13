nbh = int(input("indiquer le nombre d'heures travaillées"))
sh = float(input("donner le taux horaire"))

if nbh< 160:
    salaire = nbh * sh
elif nbh < 200:
    salaire = (160 + (nbh-160)*1.25)*sh
else:
    salaire = (160 + 40*1.25 + (nbh-200)*1.5)*sh

print (f"pour {nbh} travaillées, vous avez gagné {salaire} euros")