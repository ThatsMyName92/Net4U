from time import sleep

a="Iliya Yeriskin"
b="iliya123@gmail.com"
c=27
print("Full name: "+a+"\nEmail: "+b+"\nAge: "+str(c))
print("\n\nFull name: "+a[::-1]+"\nAge: "+str(c*3))
print("\nChecking if your name is stored in the DB....")
sleep(2)
DB="Yana Idan Yosi Iliya Haim Moshe David"
print("Iliya" in DB) #True= Yes in the DB / False= Not in the DB