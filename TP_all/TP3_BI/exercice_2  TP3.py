print("boucle while")
from time import *
N=int(input("donner un nombre positif et supérieur a 0 : "))
while N<=0 :
    N = int(input("donner un nombre positif et supérieur a 0 : "))
while N >= 0 :
    print(N)
    N = N - 1
    sleep(0.2)
    #******************************************************************************
print("boucle for")
from time import *
N=int(input("donner un nombre positif et supérieur a 0 : "))
while N<=0 :
    N = int(input("donner un nombre positif et supérieur a 0 : "))
for i in range (N ,-1 ,-1):
    print(i)
    sleep(0.2)