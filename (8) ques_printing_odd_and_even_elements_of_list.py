#printing all odd and even elements of a list
n=int(input("Enter size of list:"))
list=[]
for i in range(n):
    x=int(input("Enter num:"))
    list.append(x)
print(list)
for i in range(n):
    if (list[i]%2==0):
        print(list[i], "is even")
    else:
        print(list[i], "is odd")