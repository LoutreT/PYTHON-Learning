import os


Money=input("Quelle quantité de monnaies voulez-vous mettre ? ")

if Money == float:
    Money=ceil(Money)
    print("c'était un float ",Money)
elif Money == str:
    Money = int(Money)
    print("c'était un string ",Money)


os.system("pause")
