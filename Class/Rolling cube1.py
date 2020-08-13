import random
from time import sleep

prize=0
print("Rolling Cubes...\n")
sleep(3)
cube1=random.randint(1,6)
cube2=random.randint(1,6)
print("First Cube=  " + str(cube1) + "\nSencond Cube=  " + str(cube2))
if str(cube1)==str(cube2):
    if cube1==6:
        prize=prize+1000
    else:
        prize=prize+100
elif cube1==1:
    if cube2==2:
        prize=prize+20
    else:
        prize=prize+5
elif cube2==2:
    prize=prize+15
else:
    print("Try next time...")

sleep (2)
print("Your Prize is: " +str(prize)+ "$\nYour Prize is: " + str(prize*3.5) + "NIS")
