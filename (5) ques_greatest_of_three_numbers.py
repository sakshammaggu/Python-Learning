#greatest of three numbers
x=int(input("Enter num1:"))
y=int(input("Enter num2:"))
z=int(input("Enter num3:"))
if ((x>y)and(x>z)):
    print(x,"is largest")
elif ((y>x)and(y>z)):
    print(y,"is largest")
else:
    print(z,"is largest")