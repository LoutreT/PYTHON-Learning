import os
# On importe le module os pour évier la fermeture immédiate à la fin de
#l'execution

def TableDe64CasesDeRiz(nb,x) :

    nb= 2
    x = 1
    y = 1
    z = 0
    i = 0  # le i est préprogrammer pour lancer l'itération, c'est à dire augmenter d'un point à chaque tour de boucle de calcul.

    while i < 64 :
        i += 1
        y=(x * 2)
        print("ligne ",i," : ",x," x ",2," = ",y)
        x=y

        # print("le total des grains de riz est de ",z)

TableDe64CasesDeRiz(2,64)




os.system('pause')
