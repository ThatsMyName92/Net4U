''''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
'''


num = int(input("Choose a number 1-5:"))
num1 = int("%s" % (num))
num2 = int("%s%s" % (num,num))
num3 = int("%s%s%s" % (num,num,num))
print(num1+num2+num3)
