# -*-coding:Latin-1 -*

import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec le 
          # syst�me d'exploitation

from multipli import *

# test de la fonction table


nb=input("choisis un nombre")
os.system("pause")
nb = int(nb)   # permet de s'assurer d'avoir un integer au lieu d'un string pour la variable
               # sinon �a ne marche pas !
table(nb)

# On met le programme en pause pour �viter qu'il ne se referme (Windows)
os.system("pause")
