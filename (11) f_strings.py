name="saksham"
country="India"

text1="My name is {} and i am from {}"
print(text1.format(name, country))

text2=f"My name is {name} and i am from {country}"
print(text2)

text3=f"My name is {{name}} and i am from {{country}}"
print(text3)

price=4.989112
print(f"price={price:.2f}")
print(f"price={price:.3f}")
print(f"price={price:.4f}")

a=int(input("Enter number:"))
print(f"Multiplication Table of {a}")
for i in range(1, 11):
    print(f"{int(a)}x{i}={int(a)*i}")