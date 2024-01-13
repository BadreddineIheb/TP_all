
date = input("Veuillez entrer une date au format jjmmaaaa : ")
while len(date) != 8:
    print("Format de date incorrect. La date doit être au format jjmmaaaa.")
    date = input("Veuillez entrer une date au format jjmmaaaa : ")
jour = int(date[:2])
mois = int(date[2:4])
annee = int(date[4:])
bissextile=annee
if mois < 1 or mois > 12 or jour < 1:
    print("incorrecte")
elif mois in [1, 3, 5, 7, 8, 10, 12] and jour > 31:
    print("incorrecte")
elif mois in [4, 6, 9, 11] and jour > 30:
    print("incorrecte.")
elif mois == 2:

    if (bissextile  % 4 == 0 and bissextile % 100 != 0) or (bissextile % 400 == 0) and jour > 29:
        print("incorrecte")
    elif not (bissextile  % 4 == 0 and bissextile % 100 != 0)or (bissextile % 400 == 0) and jour > 28:
        print("incorrecte")
    else:
        print("correcte")
else:
    print("correcte")
