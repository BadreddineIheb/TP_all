Name1 = input("saisir le nom de la première personne ")
PR1 = input("saisir le prénom de la première personne ")
Name2 = input("saisir le nom de la seconde personne ")
PR2 = input("saisir le prénom de la seconde personne ")

if (Name1 < Name2) or (Name1==Name2 and PR1 < PR2):
    print(f"personne 1 : {str.capitalize(PR1)} {str.upper(Name1)}")
    print(f"personne 2 : {str.capitalize(PR2)} {str.upper(Name2)}")
else:
    print(f"personne 1 : {str.capitalize(PR2)} {str.upper(Name2)}")
    print(f"personne 2 : {str.capitalize(PR1)} {str.upper(Name1)}")

