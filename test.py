#here we are trying to get filename by using input

fn = input("Input the name of the file here: ")

#Here is a different way to do it in less lines by combining the code. We will not give any variable name to the function open() and will directly open the file to be read in the print command.
print(open(fn).read())
