

V=input("Quel est le voltage ? ")
A=input("Quel est l'ampérage ?")

try :
  V=int(V)
  A=int(A)

except TypeError :
    print("Il y a erreur, on demande uniquement un nombre entier, sans virgule")

except ZeroDivisionError :
    print("La variable que vous avez donné vaut zéro, ce n'est pdonc pas calculable ! ")

# Ci-dessous : Toutes erreurs confondues :

except TypedError as ErrorConstatee:
    print("Voici l'erreur à identifier : ", ErrorConstatee)

else:
    print("la résistance est de ",(V/A))
