# raising custom value error for number
a=int(input("Enter only even number:"))
if (a%2!=0):
    raise ValueError("This number is not Even")
else:
    print("This is Even number")

# raising custom value error for string
str=input("Enter string:")
if (str=='quit'):
    raise ValueError("You Can't quit")
else:
    print("You have entered string:",str)