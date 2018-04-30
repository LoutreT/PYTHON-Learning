
import os


V = input("V ? ")
V = int(V)

R = input("R ? ")
R = int(R)

I = input("I ? ")
I = int(I)



if (R == 0) :
  print("R vaut = ",(V/I)," ohms")

if (I == 0) :
  print("I vaut = ",(V/R)," ampères")

if (V == 0) :
  print("V vaut = ",(R*I)," volts")


os.system("pause")
