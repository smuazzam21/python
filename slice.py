s1="ram,sales,100"
s2="kumar,prod,300"
s3="Arun,HR,400"

total = (int(s1[-3:]) + int(s2[-3:]) + int(s3[-3:]))
print("Emp name is : {}  Cost is :{}".format(s1[0:3],s1[-4:]))
print("Emp name is : {}  Cost is :{}".format(s2[0:5],s1[-4:]))
print("Emp name is : {}  Cost is :{}".format(s3[0:4],s1[-4:]))
print ("-------- Total cost is : {} ----------------".format(total))