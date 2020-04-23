print("I will now count my chickens:")

#This is division first and then addition, 30/6 is 5 so answer will be 30.0 because division returns a floating point number
print("Hens", 25 + 30 / 6)

#Here we follow BODMAS with modulas thrown in. SO 25 * 3 will be 75 and 75%4 will have 3 as remainder so answer will be 97
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

#Here will will follow BODMAS again, 4%2 returns 0 and 1/4 is .024. So the equation becomes 6 - 5 + 0 - 0.25 + 6
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)


print("Is it true that 3+5 < 5-7?")

print(3 + 2 < 5 - 7)

print("What is 3+2?", 3 + 2)
print("What is 5-7", 5 - 7)

print("Oh, thats why it is false.")

print("How about some more.")

#This check only gives you True or False
print("Is it greater?", 5 > -2)

#Here it wont say greater or smaller but rather checks if the state is true or false
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal", 5 <= -2)
