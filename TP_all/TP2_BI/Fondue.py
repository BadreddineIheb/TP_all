BASE=4
formage=800.0
eau=2
ail=2
pain=400
nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
formage=formage*nbConvives / BASE
eau=eau*nbConvives / BASE
ail=ail*nbConvives / BASE
pain=pain*nbConvives / BASE
print("Poure faire une fondue fribourgeoise pour",nbConvives,"personnes, il vous faut :")
print("- ",formage,"gr de formage")
print("- ",eau,"dl d'eau")
print("- ",ail,"gousse(s) d'ail")
print("- ",pain,"gr de pain")
