"""
This program is the foundations for a text adventure game using python.
Authors: K. Fresonke, SunOfLife1
Last Updated: Apr 02, 2025
"""

# A method is a way to make your code easier to read, or it can be
# used to do the same process multiple times without repeating many lines
# def is used to make a method by going def ___():
# Anything within the method will happen whenever the method is called


def opening_talk():
    print("Hello traveller!")

    name = input("What is your name?\n")

    print(name + ", I hope you're ready to go on an adventure!")


def ghost_town():
    print(
        "\nTobey: Welcome to the town of Blanchester! We haven't had visitors"
        + " in fifty years. Why do you come here?"
    )

    questioning = True
    while questioning:
        why_come_here = input(
            "\n1: To steal all your gold!\n2: To help get rid"
            + " of your scary ghosts.\n3: I just wanted to learn your history!"
        )
        if why_come_here == "1":
            print("\nTobey: We don't have anything for you! Gone get!")
            questioning = False
        elif why_come_here == "2":
            ghost_hunting()
            questioning = False
        elif why_come_here == "3":
            history_of_ghost_town()
            questioning = False
        else:
            print("Invalid Input: Try again")
            questioning = True


def ghost_hunting():
    print(
        "\n**********************************"
        + "\nGhost hunting chosen... Continue the story from here"
    )


def history_of_ghost_town():
    print(
        "\n**********************************"
        + "\nHistory of town chosen... Continue the story from here"
    )


opening_talk()

print("\nAre you ready to go to the ghost town?")

# A variable an a while loop can be used to ask for specific values only
asking = True
while asking:
    adventure_start = input("Ghost Town: G\nExit Game: E\n")

    # After asking the user if they want to go to the ghost town or exit
    # the program will either run the ghost_town() method or exit the program

    if adventure_start == "G" or adventure_start == "g":
        asking = False
        ghost_town()
    elif adventure_start == "E" or adventure_start == "e":
        asking = False
        exit()
    else:
        print("Invalid Input: Try Again")
