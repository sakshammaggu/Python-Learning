# else with for loop
list1=[1, 2, 3, 4, 5, 6]
for i in range(len(list1)):
    print(f"list[{i}]=", list1[i])
else: #---->else keyword can only be used with loops as the loop is not breaked
    print("End!")

print("\n")

# else with for loop
list2=[1, 2, 3, 4, 5, 6]
for j in range(len(list2)):
    if (j==3): #--->loop is breaked here
        break
    else:
        print(f"list[{j}]=", list2[j])
else: #---->else keyword can only be used with loops as the loop is breaked
    print("End!")

print("\n")

# else with while loop
list3=[1, 2, 3, 4, 5, 6]
k=0
while(k<len(list3)):
    print(f"list[{k}]=", list3[k])
    k+=1
else: #---->else keyword can only be used with loops as the loop is not breaked
    print("End!")

print("\n")

# else with while loop
list4=[1, 2, 3, 4, 5, 6]
l=0
while (l<len(list4)):
    if (l==3): #--->loop is breaked here
        break
    else:
        print(f"list[{l}]=", list4[l])
        l+=1
else: #---->else keyword can only be used with loops as the loop is breaked
    print("End!")