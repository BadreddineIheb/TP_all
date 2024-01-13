liste=[5, 2, 4, 8, 1, 3]
for i in range(len(liste)):
    min = i
    for j in range(i+1, len(liste)):
        if liste[j] < liste[min]:
            min = j
    liste[i], liste[min] = liste[min], liste[i]
    print(liste)
"""########################################"""""""""

print(sorted(liste))
"""########################################"""""""""

liste.sort()
