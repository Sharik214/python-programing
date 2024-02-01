#first what is type casting in python
#The conversion of one data type into other datatype is known as type casting in python
#example
a="10"
b="2"
print(a+b)#output are 102           #[note]why i write type casting , because in python input get only in python only string data type.
                                    #you must be writen typecasting:


print(int(a)+int(b))#output 12
#there are two types of typing casting in python
#first->explicit which conversion means as programer i am doing it with my own free well
#example
string="15"
number=7
string_number=int(string)
sum=string+string_number
print("The sum of both number is:",sum)
#secound->implicit which converts python it on its own
#example
c=1.9
d=8
print(c+d)
