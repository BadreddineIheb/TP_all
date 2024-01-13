print("exercice A")
N=int(input("donner un entier: "))
S=0
for i in range (0,N+1) :
    S=S+i
print(" la somme des entiers naturels (de 0 à",N,"inclus) est:",S)



          #************************************************




print("exercice B")
N = int(input("donner un entier: "))
while N!=100 :
    N=int(input("donner un entier (100 pour sortir): "))
print("la boucle est terminé")




          #************************************************


print("exercice C")
NID=0 #Le nombre de valeurs inférieur strictement à 10
NI=0 #Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15
NSQ=0 #Le nombre de valeurs supérieur ou égale à 15
for i in range (0,10):
    X=float(input("donner un nombre : "))
    while X > 20 or X <0 :
        X = float(input("donner un nombre : "))
    if X < 10 :
        NID = NID+1
    elif X >=10  and X < 15 :
        NI = NI+1
    else :
        NSQ = NSQ+1
print("Le nombre de valeurs inférieur strictement à 10 est: ",NID)
print("Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est: ",NI)
print("Le nombre de valeurs supérieur ou égale à 15 est: ", NSQ)



          #************************************************



print("exercice D")
X=int(input("donner un nombre:"))
while X<1 :
    X = int(input("donner un nombre supérieur a 1:"))
N=0
i=0
while N <= X :
        i+=1
        N=N+i
print("le nombre recherché est : " ,i-1)


