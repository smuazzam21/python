# dev/sda1 - valid
# dev/sda2 - valid


import re
partition = input("Enter partion :")

pattern = "^/dev/sd[abd][1-4]"

if (re.search(pattern,partition)):
    print("Valid partition")
else:
    print("Not a valid partion")



