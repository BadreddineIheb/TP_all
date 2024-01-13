from time import sleep
h_1=0
h_2=0
HA=int(input("Donnez l’heure de début de la location (un entier) : "))
while HA>24 or HA<0 :
    print("Les heures doivent être comprises entre 0 et 24 !")
    HA = int(input("Donnez l’heure de début de la location (un entier) : "))
HF=int(input("Donnez l’heure de fin de la location (un entier) : "))
while HF>24 or HF<0 :
    print("Les heures doivent être comprises entre 0 et 24 !")
    HF=int(input("Donnez l’heure de fin de la location (un entier) : "))
while HF==HA:
    print("Attention ! l’heure de fin est identique à l’heure de début.")
    HF = int(input("Donnez l’heure de fin de la location (un entier) : "))
while HA > HF :
    print("Attention ! le début de la location est après la fin")
    HA = int(input("Donnez l’heure de début de la location (un entier) : "))
for i in range (HA,HF):
    if i < 7 or i >=17 :
        h_1 = h_1 + 1
    else :
        h_2 = h_2 + 1
if h_1!=0 :
    print(h_1, "heure(s) au tarif horaire de 1.0 euro(s).")
if h_2!=0 :
    print(h_2, "heure(s) au tarif horaire de 2.0 euro(s).")
MT=(h_1*1)+(h_2*2)
print("Le montant total à payer est de : ",MT)

