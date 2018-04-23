# -*-coding:Latin-1 -*

import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec votre 
          # système d'exploitation

from multipli import *

# test de la fonction table
table()
nb=input("choisis un nombre") 
os.system("pause")
print (nb)
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
