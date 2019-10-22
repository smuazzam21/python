'''
pages = [("www.python.org","www.google.com"),["www.oracle.com"],("www.example.com","www.test1.com")]

modify ---> python.org ===> python.com
        ----> google.com ===> google.co.in

add a new url ---> ["www.oracle.com","www.ab.com","www.rpm.com"]

display example.com string

'''
pages = [("www.python.org","www.google.com"),["www.oracle.com"],("www.example.com","www.test1.com")]


firstList = list(pages[0])
firstList[0] = "www.python.com"
firstList[1] = "www.google.co.in"
pages.pop(0)
pages.insert(0,tuple(firstList))

pages[1].append("www.ab.com")
pages[1].append("www.rpm.com")

print(pages)

print(pages[2][0])


