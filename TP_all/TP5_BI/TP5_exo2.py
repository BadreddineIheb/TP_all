notes=[]
for i in range (5):
    message = input(f"veuillez entrer la note du module {i} et le ocefficient correspondant : ")
    notes.append(message.split (" "))
somme=0
message = "\n"
coeff = 0
valid = True
for i in range(5):
    if float(notes[i][0]) < 8 :
        valid =False
        message += f"Note {i} < 8 \n"
    somme += float(notes[i][0])*float(notes[i][1])
    coeff += float(notes[i][1])

somme = somme/coeff
if (somme < 10):
    valid = False
    message += f"Moyenne {somme:.2f}< 10 \n"

if valid == True:
    print(f"vous avez validé votre année avec la moyenne {somme:.2f}")
else:
    print(f"vous n'avez pas validé votre année avec les problème suivants {message}")
