#WAP
# Read a enployee name frm stdin
## test emp nam is empty string or not 
## if empty --> display message (Empty string)
## if non - empty -- show char length

## Read N value test input N value is above500
## if N>500 read a customer name
### if cust name IBM -- > display N and Customer name
### if cust name Oracle -- display N and Customer name 
####  Invali customer
# invalid value of N

empName = input("Enter emp name : ")

if(len(empName) == 0):
    print("Empty String")
else:
    print("Char length : {}".format(len(empName)))

print("2nd part")

N = int(input("Enter value for N: "))
if(N > 500):
    customerName= input("Enter customer name : ")
    if(customerName == "IBM"):
        print ("Customer name is IBM")
        print ("Value of N is :{}".format(N))
    elif(customerName == "Oracle"):
        print ("Customer name is Oracle")
        print ("Value of N is :{}".format(N))

    else:
        print("Not a valid customer")
else:
    print("Not a valid value for N")