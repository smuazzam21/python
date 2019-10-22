#Reading Data from file
# open existing file  --> fileobject fh = open("inputfile",mode)
# file oject  - > read() --> "str"
#                /readlines()
# close file fh.close

fh = open("first.py","r")
print(fh.readlines())

fh.close
