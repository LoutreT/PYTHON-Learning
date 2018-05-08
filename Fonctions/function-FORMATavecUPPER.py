import os

prenom = "Vincent"
nom = "Nassaux"
ville = "Bruxelles"


print("Je m'appelle {0} {1} et j'habite {2}.".format(prenom, nom, ville))

print(\
  "Je m'appelle {0} {1} \
({3} {0} pour l'administration) \
et j'habite {2}.".format(prenom, nom, ville, nom.upper()))

# ce slash "\" me permet de continuer de programmer à la ligne suivante

os.system("pause")
