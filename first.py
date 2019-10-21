'''
WAP 
---------

Declare and initialize employee details - name , dept , eid , place , cost
using print() to display details
using single print() - line separator

'''

name = "Muazzam"
dept = "HCM"
eid = 58128
place = "Oracle Tech Hub"
cost = 100000.00

print("Name of employee is:",name)
print("Department name is:",dept)
print("Employee Id is :",eid)
print("Cost of Employee :",cost)
print("\n")
print("\n")
print("\n")
print("Now trying single statement")
print("\n")
print("\n")
print("\n")
#comma style
print("Name of employee is:",name,"\nDepartment name is:",dept,"\nEmployee Id is :",eid,"\nCost of Employee :",cost)

#control seq
print("\n")
print("\n")
print("\n")
print("Now control seq")
print("Name of employee is:%s \n Department name is:%s\n Employee id is : %d\n Cost of employee :%f"%(name,dept,eid,cost))

#format style
print("\n")
print("\n")
print("\n")
print("Now format seq")
print('''Name value : {} 
    dept value : {} 
    place value {}'''.format(name,dept,place))

