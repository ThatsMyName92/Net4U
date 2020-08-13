import random
from time import sleep

win=[]
turn=int(input("1 line for 3 NIS\nHow much Money do you have? "))//3

######################Random - 6 to win###################
print("Printing the 6 numbers...\n")
sleep(4)
counter=0
while(counter <=6 ):
    num=random.randint(1,37)
    if(num not in win):
        win.append(num)
        counter +=1
    else:
        continue

print("The winning numbers are:\n" + str(win) + "\n")

###############the game##############33
big_money=0
print("Now we will check your rows...\n")
sleep(2)
for i in range(turn):
    row = []
    counter2 =0
    count_prize=0
    while (counter2 < 6):
        num2 = random.randint(1,37)
        if (num2 not in row):
          row.append(num2)
          counter2 += 1
        if(num2 in win):
            count_prize+=count_prize
        else:
            continue

###############3Print Prize###############
    sleep(1)
    print("This round's numbers are:\n" + str(row) + "\nCalculating your prize...\n")
    sleep(1)
    if(count_prize==3):
        print("You won 10 NIS\n")
        big_money=big_money+10
    elif(count_prize==4):
        print("You won 100 NIS\n")
        big_money=big_money+100
    elif(count_prize==5):
        print("You won 5000 NIS\n")
        bing_money=big_money+5000
    elif(count_prize==6):
        print("You won 1,000,000 NIS\n")
        big_money=big_money+1000000
    else:
        print("Try next time...")

print("###### You Won " + str(big_money) + " NIS ######")
input("Press Enter to Exit")


