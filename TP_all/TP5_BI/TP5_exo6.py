
chaine = input("saisir une chaine de moins de 100 caractères (sinon les derniers ne seront pas pris en compte ")

count = 0
for i in chaine:
    count+=1


print(f"la chaine contient {count} lettres")

count = 0
for i in range(len(chaine)):
    if chaine[i] in {'i','a','e','o','u','y'}:
        count +=1
print (f"la chaine contient {count} voyelles, cela représente {round(count/len(chaine)*100,1)} % du texte")

subchaine='wagon'

