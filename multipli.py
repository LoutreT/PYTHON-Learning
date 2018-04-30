# -*-coding:Latin-1 -*

import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec votre 
          # syst�me d'exploitation

"""module multipli contenant la fonction table"""

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'� max * nb"""
    i = 0
    while i < max:
        i += 1
        print(i, " * ", nb, "=", (i * nb))




# test de la fonction table
if __name__ == "__main__":
    table(4)    #ici indent� apr�s la fonction de dessus




# On met le programme en pause pour �viter qu'il ne se referme (Windows)
os.system("pause")
