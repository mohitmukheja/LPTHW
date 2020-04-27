#Here we are printing a script and then end syntax at the end helps the person to input the value of the variable age in the same line as the question. Essentially we are asking the person to input the value of variables and then printing them in the last statement.
#If we do not print any text the syntax will run and screen will be blank asking for a value to be input. So thats why it makes sense to print a question.

print ("How old are you?", end ='')
age = input()
print ("How tall are you?", end ='')
height = input()
print ("how much do you weight?")
weight = input()
print(f"So, you are {age} old, {height} tall and {weight} heavy.")

#Input is used to ask value from the person to collect data. rather than printing a script for asking a value, we can simply add a script in input function to ask for the value as below. This will reduce code by 1 line.
val = input("Enter your age ")
print (f"So your age is {val}")

#Lets do math
x = int(input("Input value of x: "))
y = int(input("Input value of y: "))
z = x + y
print (f"The sum of {x} + {y} is : {z}")
print ("The sum of x + y is :", x + y)

a, b = input("Enter Values: ") .split()
print (a)
print (b)
