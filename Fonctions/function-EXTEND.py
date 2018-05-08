import os


# CREATION D'UNE PREMIERE LISTE, je la nomme 'PremiereListe' ;-)

PremiereListe = [0, 1, 2, 3, 4, 5]
print(PremiereListe)



# CREATION D'UNE DEUXIEME LISTE EN VUE DE L'ASSOCIER A L'AJOUTER A LA PREMIERE LISTE :

SecondeListe = [6, 7, 8, 9, 10, 11]
print(SecondeListe)



# ET MAINTENANT ON ASSOCIE LES LISTE

PremiereListe.extend(SecondeListe)
print(PremiereListe)


#--------------------------------------------------------------------------------------




SeptiemeListe = [12, 13, 14, 15, 16, 17]


#AUTRE METHODE D'ADDITION ENTRE 2 LISTES :

PremiereListe += SeptiemeListe
print(PremiereListe)



os.system("pause")
