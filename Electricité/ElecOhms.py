import os

V=input("Quel est le voltage ? ")
A=input("Quel est l'ampérage ?")

try :
  V=int(V)
  A=int(A)
  R=(V/A)

# Ci-dessous les erreurs classiques :

except TypeError :
    print("Il y a erreur, on demande uniquement un nombre entier, sans virgule")

except ZeroDivisionError :
    print("La variable que vous avez donné vaut zéro, ce n'est pdonc pas calculable ! ")

except NameError :
    print("Vous avez entré une valeur non numérique")

finally:
    print("la résistance est de ",(R)," Ohms")


os.system("pause")
