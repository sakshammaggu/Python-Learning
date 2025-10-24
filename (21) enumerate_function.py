n=int(input("Enter number of students: "))
marks=[]

for i in range(n):
    x=int(input("Enter marks of student %d:"%(i+1)))
    marks.append(x)
print(marks)

for index1, value1 in enumerate(marks):
    print(index1, value1)

for index2, value2 in enumerate(marks):
    print(f"marks[{index2}]={value2}")