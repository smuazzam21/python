# WAP in python
# =========================
# read a student name
# read marks in 3 subjects
# Calculate sum of 3 subjects and average of 3 subjects
# using single print() - display name , subject marks
# total and average
# dont use \n

name = input("Enter student's name : ")
sub1 = float(input("Enter marks in Subject 1: "))
sub2 = float(input("Enter marks in Subject 2: "))
sub3 = float(input("Enter marks in Subject 3: "))

total = sub1 + sub2 + sub3

average = total / 3

print(''' -----------------------
Name of the student : {}
Marks in Subject 1 : {}
Marks in Subject 2 : {}
Marks in Subject 3 : {}
-----------------------------
Total Marks :{}
Average : {}'''.format(name,sub1,sub2,sub3,total,average))