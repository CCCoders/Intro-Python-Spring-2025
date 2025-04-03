"""
This program is lays out the foundation for a text adventure game.
Authors: K. Fresonke, SunOfLife1
Last Updated: Apr 02, 2025
"""


# This is a function. Functions let you write some code without executing it right away.
# They can be used to make your code easier to read, and to repeat the same action multiple
# times without typing it all out every time.

# This function greets the user, asks for their name, and then prompts them to either play
# the Ghost Town story or exit the program.
def opening():
    print("Hello traveller!")

    print("What is your name?")
    name = input("> ")

    print(name + ", I hope you're ready to go on an adventure!")

    print()
    print("Are you ready to go to the ghost town?")

    # Here we have a "while" loop. This repeats everything inside the loop while a condition
    # is true, sorta like an if statement. By setting the "asking" variable to false only when
    # the user inputs an answer the program recognizes, we can make the program keep asking the
    # user for an input until they input something we want.
    asking = True
    while asking:
        print("Ghost Town: G")
        print("Exit Game: E")
        adventure_start = input("> ")

        # After asking the user if they want to go to the ghost town or exit
        # the program will either run the ghost_town() function or exit the program

        if adventure_start.lower() == "g":
            asking = False
            ghost_town()
        elif adventure_start.lower() == "e":
            asking = False
            exit()
        else:
            print("Invalid input. Try again.")


def ghost_town():
    print()
    print("Tobey: Welcome to the town of Blanchester! We haven't had visitors" +
          "in fifty years. Why do you come here?")

    # This is another "while" loop where the program stops looping only if the user
    # inputs a recognized value, this time using the "questioning" variable
    questioning = True
    while questioning:
        print()
        print("1: To steal all your gold!")
        print("2: To help get rid of your scary ghosts.")
        print("3: I just wanted to learn your history!")
        why_come_here = input("> ")

        if why_come_here == "1":
            print()
            print("Tobey: We don't have anything for you! Gone get!")
            questioning = False
        elif why_come_here == "2":
            ghost_hunting()
            questioning = False
        elif why_come_here == "3":
            history_of_ghost_town()
            questioning = False
        else:
            print("Invalid input. Try again.")


def ghost_hunting():
    print()
    print("**********************************")
    print("Ghost hunting chosen... Continue the story from here")


def history_of_ghost_town():
    print()
    print("**********************************")
    print("History of town chosen... Continue the story from here")


# This actually executes the code inside the "opening" function
opening()
