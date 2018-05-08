import os


#-----------------------------------------------------------
# POUR UNE SIMPLE VALEUR :

ValeurExemple = 35
print(ValeurExemple)


del ValeurExemple
print("Resultat : _" + "C'est effacé!")



#-----------------------------------------------------------
# DANS UNE LISTE :

ValeurLISTE = ['A', 'B', 'C', 'D', 'Z', 'E']
print(ValeurLISTE)

del ValeurLISTE[4]
print(ValeurLISTE)





os.system("pause")
