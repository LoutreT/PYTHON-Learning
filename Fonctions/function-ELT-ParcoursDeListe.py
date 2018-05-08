import os


# METHODE BASIQUE POUR DEBUTANT :

MaListe = ["- Julie", "- Nancy", "- CarolineLC","- SophieDT"]

i = 0
while i < len(MaListe):
  print(MaListe[i])
  i += 1


#------------------------------------------------------------
# CETTE METHODE EST RECOMMANDEE :

print("-------------------")

for elt in MaListe:
  print(elt)
#-----------------------------------------------------------




os.system("pause")
