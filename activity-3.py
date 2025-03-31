num1 = input("First Number to calculate: ")

while not num1.isdigit():
    num1 = input("First Number to calculate: ")

num2 = input("Second Number to calculate: ")

while not num2.isdigit():
    num2 = input("Second Number to calculate: ")

operation = input("Operation: ")

while operation not in ("+", "-", "/", "*"):
    operation = input("Operation: ")
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
