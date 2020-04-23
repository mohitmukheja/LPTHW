#Set variable as string
print("Mary had a little lamb.")

#This is the same as what we did in last exercise where we leave format string in a variable and then we use.format() to call out the value of the variable below instead of defining a variable before as snow and calling its value here we are calling value of {} as a string snow. If we remove ''s it iwll give error as we havent defined before
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")

#Here a period is a string and * makes it repeat it for 10 times
print("."*10) #what did it do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end. Try removing it to see what happens

#Here the comma after the end6 helps to append the output of the next print command in the same line with a space as a separater. That can be replaced with anything in the inverted commas.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

#Here I have modified the line 28 in a different way. If we do not use sep function, it will automatically put a space as a separater between various variables while printing. However if we want to remove the space, we can use sep function and in the inverted commas dont put anything as below. This will make Burger as one word.
print(end7,end8,end9,end10,end11,end12, sep='')
