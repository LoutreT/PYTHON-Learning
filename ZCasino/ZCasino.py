# Ce fichier abrite le code du ZCasino, un jeu de roulette adapté


import os
from random import randrange
from math import ceil



argent = 1000
continuerpartie = True

print("On s'installe autour de la roulette de casino avec",argent,"euros")

while continuerpartie:
  nombremise = -1
  while nombremise > 0 :
    nombremise = input("quel somme vous déposez ?") #On ne met 2 points(:) parce que
    # parce que ce n'est pas une fonction, c'est une égalité, une assignation.
    try:
      nombremise = int(nombremise)
    except valueError:
      print("Vous n'avez pas choisi de nombre")
      nombremise = -1
      continue
    if nombremise < 0:
      print("ce nombre est négatif")
    if nombremise > 49:
      print("Ce nombre est supérieur à 49")

#randrange(50)

