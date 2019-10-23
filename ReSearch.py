import re
with open("fsinfo.log","r") as fh:
    for var in fh.readlines():
        var = var.strip()
        if(re.search("^root",var,re.I)):
            print(var)

print("="*20 +" Ends With " +"="*20)

with open("buildCoreBMT.out","r") as fh1:
    for var in fh1.readlines():
        var = var.strip()
        if(re.search("antlib:oracle.anttasks:copyFilesFromCustomtaskjar$",var)):
            print(var)

print("="*20 +" Exact Match " +"="*20)

with open("buildCoreBMT.out","r") as fh2:
    for var in fh2.readlines():
        var = var.strip()
        if(re.search("^BUILD SUCCESSFUL$",var)):
            print(var)
print("="*20 +" Dot Match " +"="*20)

with open("fsinfo.log","r") as fh:
    for var in fh.readlines():
        var = var.strip()
        if(re.search("^r.",var,re.I)): #starts with r followed by any char
            print(var)

print("="*20 +" * Match " +"="*20)

with open("fsinfo.log","r") as fh:
    for var in fh.readlines():
        var = var.strip()
        if(re.search("^a.*bgl",var,re.I)): #starts with a followed by any number chars
            print(var)

print("="*20 +" Charactee match " +"="*20)

with open("fsinfo.log","r") as fh:
    for var in fh.readlines():
        var = var.strip()
        if(re.search("^[=]",var,re.I)): #starts with a followed by any number chars
            print(var)