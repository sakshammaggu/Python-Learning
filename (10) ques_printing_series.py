#printing series
# 2,22,222,2222,.......n terms
n=int(input("Enter num of terms:"))
x=int(input("Enter number:"))
y=x
for i in range(1, n+1):
    print(x)
    x+=(y*(10**i))