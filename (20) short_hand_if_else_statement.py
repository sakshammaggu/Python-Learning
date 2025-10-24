# general way of writing short hand if-else statement
# result = value_if_true if (condition) else value_if_false

a=int(input("Enter num1:"))
b=int(input("Enter num1:"))
print("a greater than b") if (a>b) else print("a equal to b") if (a==b) else print("a less than b") if (a<b) else ""

c=int(input("Enter num1:"))
d=int(input("Enter num1:"))
print("c greater than d") if (c>d) else ""
print("c lesser than d") if (c<d) else ""

e=10 if (a<b) else 0
print(e)
f=10 if (c>d) else 0
print(f)