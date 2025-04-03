"""
This program is the foundations for a text adventure game using python.
@Author K. Fresonke
Last Updated: Mar 31, 2025
"""

# A method is a way to make your code easier to read, or it can be
# used to do the same process multiple times without repeating many lines
# def is used to make a method by going def ___():
# Anything within the method will happen whenever the method is called


# This is the main method for the game
def game():
    openingTalk()

    print("\nAre you ready to go to the ghost town?")

    # A variable an a while loop can be used to ask for specific values only
    asking = True
    while asking == True:
        adventureStart = input("Ghost Town: G\nExit Game: E\n")

        # After asking the user if they want to go to the ghost town or exit
        # the program will either run the ghostTown() method or exit the program

        if adventureStart == "G" or adventureStart == "g":
            asking = False
            ghostTown()
        elif adventureStart == "E" or adventureStart == "e":
            asking = False
            exit()
        else:
            print("Invalid Input: Try Again")


def openingTalk():
    print("Hello traveller!")

    name = input("What is your name?\n")

    print(name + ", I hope you're ready to go on an adventure!")


def ghostTown():
    print(
        "\nTobey: Welcome to the town of Blanchester! We haven't had visitors"
        + " in fifty years. Why do you come here?"
    )

    questioning = True
    while questioning == True:
        whyComeHere = input(
            "\n1: To steal all your gold!\n2: To help get rid"
            + " of your scary ghosts.\n3: I just wanted to learn your history!"
        )
        if whyComeHere == "1":
            print("\nTobey: We don't have anything for you! Gone get!")
            questioning = False
        elif whyComeHere == "2":
            ghostHunting()
            questioning = False
        elif whyComeHere == "3":
            historyOfGhostTown()
            questioning = False
        else:
            print("Invalid Input: Try again")
            questioning = True


def ghostHunting():
    print(
        "\n**********************************"
        + "\nGhost hunting chosen... Continue the story from here"
    )


def historyOfGhostTown():
    print(
        "\n**********************************"
        + "\nHistory of town chosen... Continue the story from here"
    )


# Starts the game method
game()
