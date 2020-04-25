#setting a var with \t, it adds a tab
tabby_cat = "\tI'm tabbed in"
#\n splits the sentence into a lines
persian_cat = "I'm split \non a line."

#\\ simply adds a baclslash to the string
backslash_cat = "I'm \\ a \\ cat."

#Three quotes let us type whatever we want in multiple lines without getting error
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#Below I am testing various baclslash (\) commands in a string and what impact they have on the string.

#adds a baclslash
cat1 = "I am a cat \\that is a fat wearing a hat"
print(cat1)

#adds a single quote
cat2 = "I am a cat \'that is a fat wearing a hat"
print(cat2)

#adds a double quote
cat3 = "I am a cat \"that is a fat wearing a hat"
print(cat3)

#adds a backspace, so essentially removes one space.
cat4 = "I am a cat \bthat is a fat wearing a hat"
print(cat4)

#adds a new line
cat5 = "I am a cat \nthat is a fat wearing a hat"
print(cat5)

#Have no ides how exactly this one functions
cat6 = "I am a cat that is a \rfat wearing a hat"
print(cat6)

#adds a tab
cat7 = "I am a cat \tthat is a fat wearing a hat"
print(cat7)

#ASCii vertical tab but it returns a ? value in the string so dont know what it does.
cat8 = "I am a cat \vthat is a fat wearing a hat"
print(cat8)
