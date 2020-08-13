import random
from time import sleep
################## Functions ################
def menu():
    while(True):
        choise=input("Menu: \n1.Dog Details\n2.Friends List\n3.N Azzeret\n")
        if(choise=="1"):
            Dogs()
        elif(choise=="2"):
            Friends()
        elif(choise=="3"):
            Azzeret()
        else:
            print("Enter 1-3 only!!!\n")
            continue
        if(input("Do you want to exit? y/n\n")=="y"):
            break
    print("\nThanks and byebye...\n")

##### code ######
def Dogs():
    dog_name=input("Enter your Dogs name: \n")
    dog_age=int(input("Enter your Dogs age: \n"))
    print("My Dog's name: " + dog_name + "\nMy Dog's Age: " + str(dog_age*7))


def Friends():
    friend=[]
    for i in range(4):
        friend.append(input("Enter friend's name: "))
    if(input("Enter Your friend from right: ") in friend):
        print("He is inside!!\n")
    else:
        print("He isn't inside!!\n")

def Azzeret():
    num=int(input("Enter a number: \n"))
    num2=1
    for i in range(1,num+1):
        num2=num2*i
    print("\nYour N Azzeret is: " + str(num2))


####### menu ########
menu()