
import re

name = input("Enter the name :")
eid = input("Enter the Id :")


idPattern = ("^[A-E]\d{3}$")

namePattern = ("^[A-Z][a-z]+$")

if(re.search(idPattern,eid)):
    print("Valid Id")
else:
    print("Not a valid Id")

if(re.search(namePattern,name)):
    print("Valid Name")
else:
    print("Invalid Name")
