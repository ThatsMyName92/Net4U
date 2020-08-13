'''
Write a Python program to test whether a number is within 100 of 1000 or 2000
'''


def near_thousand(x):
    return ((abs(1000 - x) <= 100) or (abs(2000 - x) <= 100))


print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))
print(near_thousand(740))
print(near_thousand(1850))
print(near_thousand(950))
print(near_thousand(1200))