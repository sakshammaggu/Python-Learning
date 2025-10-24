# printing series
#   1-49
#   2-48
#    .
#    .
#    .
#   49-1
n=int(input("Enter num:"))
i=1
j=n
while ((i<=n)and(j>=1)):
    print(i, "---", j)
    i+=1
    j-=1