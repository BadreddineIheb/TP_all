from random import *
tours=0
V=randint(0,100)
A = int(input("deviner la valeur : "))
while A != V :
    if A < V:
        print("la valeur est plus grande")
    else:
        print("la valeur est plus petite")
    tours = tours + 1
    A = int(input("deviner la valeur : "))
print("la valeurs est : ",A)
print("le nombre de tours est : ",tours)