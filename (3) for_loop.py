list=["ab", "bc", 23, 24]
for i in list:
    print(i)

list1=[["a", 1], ["b", 2], ["c", 6], ["d", 8]]
for i in list1:
    if ((str(i).isnumeric())and(list1[i][i]>2)):
        print(i)