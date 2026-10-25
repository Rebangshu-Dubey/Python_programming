name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

learning_python = input("Are you learning Python? (yes/no): ").strip().lower() == "yes"             #stripping whitespace and converting to lowercase for comparison 

print("Name:", name)
print("Age:", age)
print("Height:", height, "meters")
print("Learning Python:", learning_python)