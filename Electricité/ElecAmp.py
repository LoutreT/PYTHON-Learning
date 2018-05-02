import os


V=input("Quel est le voltage ? ")
R=input("Quel est la résistance ? ")

try :
  V=int(V)
  assert V > 0 # "assert"permet de bien vérifier que la valeur n'est ni négative ni zéro

  R=int(R)
  assert R>= 0 # "assert"permet de bien vérifier que la valeur n'est pas négative

  A=(V/R)


# Ci-dessous : Toutes erreurs confondues :
except TypedError as ErrorConstatee:
    print("Voici l'erreur à identifier : ", ErrorConstatee)


finally:
    print("l'intensité est de ",(A)," Ampères")


os.system("pause")
