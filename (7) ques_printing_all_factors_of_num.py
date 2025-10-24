#printing all factors of number
n=int(input("Enter num:"))
i=1
while (i<=n):
    if(n%i==0):
        print(i)
    i+=1