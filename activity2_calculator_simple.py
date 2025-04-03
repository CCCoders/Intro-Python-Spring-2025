# Print a description of this program
print("This program is a calculator. Enter two numbers and an operation to perform, and I'll tell you the result.")

# Print empty new line
print()


num1 = input("First Number to calculate: ")

if not num1.isdigit():
    print("That's not a whole number. Exiting now..")
    exit(1)

num1 = int(num1)


num2 = input("Second Number to calculate: ")

if not num2.isdigit():
    print("That's not a whole number. Exiting now..")
    exit(1)

num2 = int(num2)


operation = input("Operation: ")

# Print empty new line
print()


if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("That operation isn't supported. Exiting now..")
    exit(1)

# Another way to print variables is by separating them with commas.
# If you do this, each variable will be printed with a space after it.
print(num1, operation, num2, "=", result)
