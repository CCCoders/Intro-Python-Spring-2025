# Print a description of this program
print("This program is a calculator. Enter two numbers and an operation to perform, and I'll tell you the result.")

num1 = input("First Number to calculate: ")

if not num1.isdigit():
    exit(1)

num2 = input("Second Number to calculate: ")

if not num2.isdigit():
    exit(1)
    
operation = input("Operation: ")

while operation not in ("+", "-", "/", "*"):
    exit(1)
    
num1 = int(num1)
num2 = int(num2)

if operation == "+":
    print(num1 + num2)
if operation == "-":
    print(num1 - num2)
if operation == "*":
    print(num1 * num2)
if operation == "/":
    print(num1 / num2)
