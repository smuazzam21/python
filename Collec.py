# Given List

emp = ["ram,sales,pune,1000","arun,prod,bglore,2000","anu,HR,hyd,3000"]

#Display Empname , woking city 
# Calc sum of emps cost
# display total cost

empl1 =[]
for e in emp:
    empl1.append(e.split(","))
cost =0 

for l1 in empl1:
    print("Employee name is : {} and working city is :{}".format(l1[0],l1[2]))
    cost += int(l1[3])

print("========================================")
print("Total Cost is : {}".format(cost))
print("========================================")
