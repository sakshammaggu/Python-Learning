#printing sum of given series i.e
# 1+4-9+16-25+36-.......n terms
n=int(input("Enter number of terms:"))
x=0
y=0
for i in range(2, n+1):
    if (i%2==0):
        x+=i**2
    else:
        y+=i**2
print("Sum of series:", 1+(x-y))