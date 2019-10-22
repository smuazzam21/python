''' Create Empty list
    using loop ( while)
    read 5 diff file names
    add input to exiting list

    display file names in format 
    1. test.txt...

    read a input file from stdin
    using membership operator
    test input file existing or not
'''

# creating empty list
filenames = []
count =0
while(count < 5):
    filename = input("Enter filename : ")
    filenames.append(filename)
    count+=1
count = 1
print("------Entered files are--------")
for v in filenames:
    print ("{}.{}".format(count,v))
    count+=1

fname = input("Enter a file name : ")

if(fname in filenames):
    print("File : {} exists".format(fname))
else:
    print("File : {} does not exists".format(fname))