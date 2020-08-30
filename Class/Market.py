'''
Market:
Tomato - 3$
Cucumber - 2$
Coca Cola - 5$
Chicken - 20$
'''
from time import sleep

print("Hello\n---------------------\nToday in the Market:\nTomato = 3$\nCucumber = 2$\nCoca-Cola = 5$\nChicken = 20$")
tomato=int(input("Enter How many Tomatos would you like? "))
cucumber=int(input("Enter How many Cucumbers would you like? "))
cola=int(input("Enter How many Coca-Colas would you like? "))
chicken=int(input("Enter How many Chickens would you like? "))
print("\n------------------\nCalculating.....\n------------------")
sleep(2)
print("\nSummery of your order:\n----------------------\nTomatos: " + str(tomato) + "\nCucumbers: " + str(cucumber) + "\nCoca-Cola: " + str(cola) + "\nChickens: " + str(chicken) + "\n----------------------")

#sum1=tomato*3
#sum2=cucumber*2
#sum3=cola*5
#sum4=chicken*20
#total=sum1+sum2+sum3+sum4
#totvat=total*1.17
sleep(2)
summery=(tomato*3)+(cucumber*2)+(cola*5)+(chicken*20)

print("\nYour Bill is: ------ " + str(summery) + "$")
print("Your Bill including VAT: ------ " + str("%.2f" % (summery*1.17)) + "$\n\n----------------------")









