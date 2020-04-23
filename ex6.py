#setting types_of_people value as 10
types_of_people = 10
#using fstring to call out variable value in a string and setting value of x as that string
x = f"There are {types_of_people} types of people."

#setting variabl values and then using fstring to call call out in a string while assinging value to variable y
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#printing value of x and y
print(x)
print(y)

#printing value of x and y in a string
print(f"I said: {x}")
print(f"I also said: {y}")

#setting value of two variables here, filarious as False and joke_evaluation as string with {} to call out the value of any variable
hilarious = False
joke_evaluation = "Isn't that joke so funny! {}"

print(joke_evaluation.format(hilarious))

#setting variable value and then concatenating it using + sign
#we can use + sign to even concatenate different string by using "s in the print function
w = "This is the left side of ..."
e = "a string with a right side."

print (w + e)

#here we text my above theory by assigning value of t to poop and then using format() to call out value of t as poop in the print function
t = "test"
r = "cute"
joke_evaluation1 = "Isn't that joke so funny! {}"
joke_evaluation2 = f"Isn't that joke so funny! {r}"
print(joke_evaluation1.format(t))
print(joke_evaluation2)
