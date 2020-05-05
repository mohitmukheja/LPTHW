#Here in this exercise, we are trying to ask the person running the script to enter the name of the file. This helps us to avoid hardcoding name of file in the script. So this file and be used to read pretty much any file so long the person running the script enters the name.


#Here we are importing value of argv from the script
from sys import argv

#argv returns what programmer enters in the script. While running the script we enter the file name so that we can assign the file to txt variable.
script, filename = argv

#here we give variable txt a function open() which inturn pulls name of the file. Additional arguments can be given to open it in write mode etc.

txt = open(filename)

#Here we are printing txt file in default mode with no parameters
print(f"Here is your file {filename}")

print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#here we are trying to get filename by using input

fn = input("Input the name of the file here: ")

#Here is a different way to do it in less lines by combining the code. We will not give any variable name to the function open() and will directly open the file to be read in the print command.
print(open(fn).read())


#below is a command to close the file.
txt.close()
txt_again.close()
