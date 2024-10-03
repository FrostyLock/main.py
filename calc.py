
python
def add(x, y, z):
    return x + y + z

def subtract(x, y, z):
    return x - y + z

def multiply(x, y, z):
    return x * y * z

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4/5): ")

numQ = float(input("Enter first number: "))
numW = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num222))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num4))
else:
    print("Invalid input")
```
