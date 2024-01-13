L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]
n=0
k=0
for i in range (0,len(L1)):
    temp = L1[i]
    for j in range (0,len(L1)):
        if temp==L1[j]:
            n=n+1
    if k<n :
        k=n
        NPF=L1[i]
    n=0

print("Le nombre le plus frequent dans la liste est le : ",NPF,"(",k,")")








""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
