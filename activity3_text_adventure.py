"""
This program is the foundations for a text adventure game using python.
Authors: K. Fresonke, SunOfLife1
Last Updated: Apr 02, 2025
"""

# A function is a way to make your code easier to read, or it can be
# used to do the same process multiple times without repeating many lines
# def is used to make a function by going def ___():
# Anything within the function will happen whenever the function is called


def opening_talk():
    print("Hello traveller!")

    print("What is your name?")
    name = input("> ")

    print(name + ", I hope you're ready to go on an adventure!")


def ghost_town():
    print()
    print("Tobey: Welcome to the town of Blanchester! We haven't had visitors" +
          "in fifty years. Why do you come here?")

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


opening_talk()

print()
print("Are you ready to go to the ghost town?")

# A variable an a while loop can be used to ask for specific values only
asking = True
while asking:
    print("Ghost Town: G")
    print("Exit Game: E")
    adventure_start = input("> ")

    # After asking the user if they want to go to the ghost town or exit
    # the program will either run the ghost_town() function or exit the program

    if adventure_start == "G" or adventure_start == "g":
        asking = False
        ghost_town()
    elif adventure_start == "E" or adventure_start == "e":
        asking = False
        exit()
    else:
        print("Invalid input. Try again.")
