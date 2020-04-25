# Here is some strange stuff, remember type it exactly.

#Here we are setting variable days as string variable with days of the week.
days = "Mon Tue Wed Thu Fri Sat Sun"

#Here we are setting variable months as Months of the year however between different words we are adding \n which add a line break before the next word.

months1 = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#If we want to move Jan to the next line all we have to do is add \n before Jan so that it moves to the next line.
months2 = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#below we are just printing both the variables and seeing the outcome.
print("here are the days:" , days)
print("Here are the months:", months1)
print("Here are the months:", months2)

#Adding three quotes enables us to continue our text in the next line without giving syntax error.
print("""
There is something going on here.
With the three double quotes.
We will be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
