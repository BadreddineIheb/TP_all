x=int(input("Entrez un nombre entier: "))
y=x%2
if x>0 and y==0:
    print("Le nombre est positif et pair")
elif x>0 and y!=0:
    print("Le nombre est positif et impair")
elif x<0 and y==0:
    print("Le nombre est négatif et pair")
elif x<0 and y!=0:
    print("Le nombre est négatif et impair")
else:
    print("Le nombre est zéro (et il est pair)")


