import time
from time import *

f=1
n=int(input("donner un nombre : "))
A=int(input("choisir la boucle a utiliser (1 pour while et 0 pour for) : "))
while A<0 or A>1 :
    A = int(input("choisir la boucle a utiliser (1 pour while et 0 pour for) : "))
Z=n
if A==1 :
     while Z!=1 :
        f=f*Z
        Z=Z-1
        print(f)
        sleep(1)
else  :
    for i in range (n,1,-1) :
        f = f * Z
        Z = Z - 1
        print(f)
        sleep(1)
print (" le factorielle de ",n," est : ",f)
