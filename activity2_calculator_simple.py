# Print a description of this program
print("This program is a calculator. Enter two numbers and an operation to perform, and it'll tell you the result.")

# Print an empty new line
print()


# Ask the user for the first number
num1 = input("Enter a whole number: ")

# Check that the text the user entered is a whole number. If it's not, print a message and exit the program
if not num1.isdigit():
    print("That's not a whole number. Exiting now..")
    exit()

# Convert the text the user entered for num1 from a string to an integer, and save it back to num1
num1 = int(num1)


# Ask the user for the second number
num2 = input("Enter another whole number: ")

# Check that the text the user entered is a whole number. If it's not, print a message and exit the program
if not num2.isdigit():
    print("That's not a whole number. Exiting now..")
    exit()

# Convert the text the user entered for num2 from a string to an integer, and save it back to num2
num2 = int(num2)


# Ask the user for the operation to perform
operation = input("Enter an operation: ")

# Print an empty new line
print()


# If the operation entered by the user is supported, save the result to a new "result" variable.
# Otherwise, print a message about the operation being not supported and exit out the program.
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
else:
    print("That operation isn't supported. Exiting now..")
    exit()

# Another way to print variables is by separating them with commas.
# If you do this, each variable will be printed with a space after it.
print(num1, operation, num2, "=", result)
