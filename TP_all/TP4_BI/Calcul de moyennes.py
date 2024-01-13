# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []
temp=0
S=0
for i in range (0,nombreEtudiants):
    temp=float(input(f"Note etudiant{i+1}: "))
    if temp<0 or temp>20 :
        print("la note doit etre entre 0 et 20")
        temp = float(input(f"Note etudiant{i}: "))
    notes.append(temp)
    S=S+temp
MDC=S/nombreEtudiants
print("Moyenne de classe : ",MDC)
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range (0,nombreEtudiants):
    print(i,"|",notes[i],"|",notes[i]-MDC)

