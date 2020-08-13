'''
Menu:
1.Print IP
2.Print Memory
3.Print Storage
4.Print CPU

'''

print("Menu:\n**Please enter your choise 1-4 ONLY**\n1.Print IP\n2.Print Memory\n3.Print Storage\n4.Print CPU")
num=input("Enter Your Choise:  ")
if num=="1":
    print("IP is: 124.123.123.123")
elif num=="2":
    print("Your Memory is: 64GB")
elif num=="3":
    print("Your Storage is:100TB")
elif num=="4":
    print("Your CPU usage is: 0.3%")
else:
    print("Please Enter 1-4 ONLY!")
