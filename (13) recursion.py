# factorial of a number using recursion
def factorial(a):
    if ((a==0)or(a==1)):
        return 1
    return a*factorial(a-1)
a=int(input("Enter num:"))
print("Factorial=", factorial(a))