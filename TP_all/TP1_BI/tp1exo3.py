jour = int(input('saisie le jour :'))        
heure = int(input("saisie l'heure :"))
minute = int(input("saisie les minutes :"))
minute_par_jour = jour * 24 * 60
minute_totales = minute_par_jour + heure * 60 + minute
print('le résultat totale des minutes écoulées depuis le début du mois sont :',minute_totales)
