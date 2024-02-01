#in python there are a special keyword, i.e input
#basic example
z=input
print(z)
#note storing only string input you must be writing type casting.
#example
'''a=input("Enter first number:"),<-entered value 23
b=input("Enter Secound number:")<-entered value 23
print(a+b)'''#ouput 2323 which is totaly wrong 
#how to solve it
a=input("Enter first number:")
b=input("Enter Secound number:")
print(int(a)+int(b))