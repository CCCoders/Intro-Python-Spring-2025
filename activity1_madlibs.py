# This is a comment! Anything in a comment is ignored when running your code.

# The "input" function displays text, then waits for the user to input something.
# By using something like "word = input("Some text")", we're saving whatever the user typed to a variable called "word".
noun = input("Enter a noun: ")
verb = input("Enter a verb ending in 'ing': ")

# This uses a print statement to display the full sentence.
# The usage of "+" combines text with our variables, so we can display sentences with the user-inputted text mixed in.
print(noun + " is " + verb)
