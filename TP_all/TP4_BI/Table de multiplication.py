from time import *
Nomber=float(input("Vous cherchez la table de multiplication de quel nombre ? "))
table=[]
for i in range (0,10):
    R= Nomber * i
    Arrondi = round(R,2)
    table.append(Arrondi)
for i in range (0,10):
    print(Nomber,"*",i,"=",table[i])