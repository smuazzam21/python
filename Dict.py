# Create empty dict
# Student name , sub1 , sub2 and sub3 as key vakue pairs
#d Display key value pair
# Modify a subject value
# Add new element (dep , depname)
# display updated dictionary
# delete sub3 key value pair


student_dic = {}

student_dic.setdefault("name","Muazzam")
student_dic.setdefault("Sub1","87")
student_dic.setdefault("Sub2","97")
student_dic.setdefault("Sub3","86")

for std in student_dic:
    #print(student_dic.get(std))
    print("{}\t{}\n".format(std,student_dic.get(std)))

student_dic["Sub1"] = 77
print("="*50)
for std in student_dic:
    #print(student_dic.get(std))
    print("{}\t{}\n".format(std,student_dic.get(std)))

student_dic.setdefault("Dept","CSE")
print("="*50)
for std in student_dic:
    #print(student_dic.get(std))
    print("{}\t{}\n".format(std,student_dic.get(std)))

student_dic.pop("Sub3")

print("="*50)
for std in student_dic:
    #print(student_dic.get(std))
    print("{}\t{}\n".format(std,student_dic.get(std)))
