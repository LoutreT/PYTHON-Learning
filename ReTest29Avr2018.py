import os
# On importe le module os pour évier la fermeture immédiate à la fin de
#l'execution

nb=input("Quelle valeur voulez-vous multiplier ? ")
nb=int(nb) #Ici on transforme en integer la variable "nb".

#ici ne pas oublier de définir la valeur de "max",
# ni de terminer la ligne de la fonction par un double point ":"
def table_de_multiplication(x,max):
    i=0
    while i<max :
        i+=1
        print(i,"x",nb,"=",(i*nb))

table_de_multiplication(nb,10) # ici 10 remplace la variable "max", elle le définit en nombre précis.


os.system('pause')
