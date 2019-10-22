#with , as


with open("myfile.txt","r") as fh:
    with open("myfile1.txt","w") as wh:
        for v in fh.readlines():
            print(v.strip())
            wh.write(v +"\n")

    

