#calculator using by python
a=input("Enter first number")
operator=input("Enter operator")
b=input("Enter secound number")
if operator=='+':
print(int(a)+int(b))
if operator=='-':
print(int(a)-int(b))
if operator=='/':
print(int(a)/int(b))
if operator=='%':
print(int(a)%int(b))
if operator=='*':
print(int(a)*int(b))
if operator=='//':
print(int(a)//int(b))
else:
print("you entered illegalone")
