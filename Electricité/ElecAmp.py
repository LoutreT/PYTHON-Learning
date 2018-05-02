
import os

V=input("Quel est le voltage ? ")
R=input("Quel est la résistance ? ")

try :
  V=int(V)

  R=int(R)

  A=(V/R)


# Ci-dessous : Toutes erreurs confondues :

except TypedError as ErrorConstatee:
    print("Voici l'erreur à identifier : ", ErrorConstatee)


finally:
    print("l'intensité est de ",(A)," Ampères")


os.system("pause")
