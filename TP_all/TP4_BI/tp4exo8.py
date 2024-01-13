dictionaire={}
dictionaire['firstname']=str(input("donner votre nom:"))
dictionaire['name']=str(input("donner votre prenom:"))
dictionaire['promo']=str(input("donner votre promo:"))
dictionaire['group']=str(input("donner votre group:"))
L1=list(dictionaire.keys())
L2=list(dictionaire.values())
L3=list(dictionaire.items())
print('les clés du dictionnaire sont :')
for i in range (len(L1)):
    print('-',L1[i])
print('les valeurs du dictionnaire sont :')
for i in range (len(L2)):
    print('-',L2[i])
print('les tuplets du dictionnaire sont :')
for i in range (len(L3)):
    print('-',L3[i])











print(f'votre nom est : {dictionaire["firstname"]}     et votre prénom est  : {dictionaire["name"]}    vous faites partie de la promo   : {dictionaire["promo"]}   et votre group est   :  {dictionaire["group"]}')


