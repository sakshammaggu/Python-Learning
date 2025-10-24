a=input("Enter number:")
print(f"Multiplication Table of {a}")
try:
    for i in range(1, 11):
        print(f"{int(a)}x{i}={int(a)*i}")
except:
    print("Invalid!")
finally: #---->finally keyword
    print("End Of Code")

print("\n")

list=[1, 2, 3, 4]
index=input("Enter index:")
try:
    print(list[int(index)])
except ValueError:
    print("Number is not entered.")
except IndexError:
    print("Index Error")
finally: #---->finally keyword
    print("End Of Code")