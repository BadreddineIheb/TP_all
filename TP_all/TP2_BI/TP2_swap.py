a=ina=input("Entrez la premiere  valeur : ")
b=inb=input("Entrez la deuxieme  valeur : ")
c=inc=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")
x=a
a=b
b=c
c=x
print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)