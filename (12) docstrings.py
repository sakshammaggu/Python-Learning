def sum(a, b):
    #-->this is a doctring
    '''This is function of sum of two numbers and this is a docstring'''
    return a+b
a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
print(sum(a,b))
print(sum.__doc__)

def product(a, b):
    return a*b
    #-->this is not a doctring
    '''This is function of product of two numbers and this is not a docstring'''
a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
print(product(a,b))
print(product.__doc__)