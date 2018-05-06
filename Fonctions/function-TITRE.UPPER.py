import os


x = input("Quels mots voulez-vous écrire pour espacer entre le début et la fin d'un titre et centrer le titre ?")

y = int(input("Quel nombre de point d'espace voulez-vous donner à votre chaine de caractère ? "))


#FORMULE :
# x = titre
# titre.upper()


print(x.upper().center(y))


os.system("pause")
