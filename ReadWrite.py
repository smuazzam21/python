'''
 - Read data from one file
 - Write the read data to a new file
'''


fr = open("buildCoreBMT.out",'r')
list1 = fr.readlines()
fr.close()

fw = open("writefile.txt",'w')

for l in list1:
    if("Total time:" in l):
        fw.write(l+"\n")

fw.close()