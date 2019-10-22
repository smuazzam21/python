
fstype ="xfs"
fsize = "2TB"
fowner ="root"


# Create a new file (fsinfo.log)
# write the string to file


#create empty list
#read data from line add each line to list
# update valyes 
# update fsinfo.log file

with open("fsinfo.log","w") as wh:
    wh.write("FS_TYPE : {}\n".format(fstype))
    wh.write(fsize +"\n")
    wh.write(fowner +"\n")
    wh.write("=====================Write Complete=======================\n")

list1 =[]
with open("fsinfo.log","r") as rh:
    list1 = rh.readlines()

print(list1)
list1.pop()

list1[0] = "newxfs"
list1[1] = "new2TB"
list1[2] = "new-root"

with open("fsinfo.log","a") as wh:
    for s in list1:
        wh.write(s +"\n")
    
    wh.write("=====================Write Complete=======================\n")
