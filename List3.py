'''
contents=["data1\n","data2\n","data3\n","data4\n","data4\n"]
display last 3 elements remove \n
display 1st 3remove \n
    
    add folloeing lines in to existing list inclide \n
        s1 = "data6"
        s2="data7"
        
using loop display all contents        
'''


contents=["data1\n","data2\n","data3\n","data4\n","data4\n"]
s1 = "data6"
s2="data7"
print("last 3 ")
for v in contents[-3:]:
    print(v.strip())
print("first 3 ")
for v in contents[0:3]:
    print(v.strip())

contents.append(s1+"\n")
contents.append(s2+"\n")

print("Entire contents")
for v in contents:
    print(v)

