# user inputs name age and income


name = input("enter your name: ")
age = int(input("enter your age: "))
income = int(input("enter your monthky income in numbers: "))


print(f"your name: {name}")
print(f"your age: {age}")
print(f"monthly income: {income}")

if age >= 18:
	print("you are eligible")
else:
	print("you are not eligible")
