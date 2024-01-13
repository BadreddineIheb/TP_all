nMax=4
taille= int(input("Quelle est la taille de vos vecteurs [entre 1 et 4] ? "))
if taille>nMax or taille<1 :
    taille = int(input("Quelle est la taille de vos vecteurs [entre 1 et 4] ? "))
v1=[]
v2=[]
temp=0
PS=0
print("Saisie du premier vecteur : ")
for i in range (0,taille):
    temp=float(input(f"v1{[i]}= "))
    v1.append(temp)
print("Saisie du second vecteur : ")
for i in range (0,taille):
    temp=float(input(f"v2{[i]}= "))
    v2.append(temp)
for i in range (0,taille):
    PS=PS+v1[i]*v2[i]
print("Le produit scalaire de v1 par v2 vaut ",PS )

