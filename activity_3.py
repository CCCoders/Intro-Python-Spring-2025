'''
This program is the foundations for a text adventure game using python.
@Author K. Fresonke
Last Updated:
'''

def openingTalk():
    print("Hello traveller!")

    name = input("What is your name?")

    print( name + ", I hope you're ready to go on an adventure!")
    print("\nAre you ready to go to the ghost town?")

def ghostTown():
    print("Tobey: Welcome to the town of Blanchester! We haven't had visitors"+
        " in fifty years. Why do you come here?")
    
    questioning = True
    while( questioning == True):
        whyComeHere = input("\n1: To steal all your gold!\n2: To help get rid"+
            " of your scary ghosts.\n3: I just wanted to learn your history!")
        if( whyComeHere == "1"):
            print("Tobey: We don't have anything for you! Gone get!")
            questioning = False
        elif( whyComeHere == "2"):
            ghostHunting()
            questioning = False
        elif( whyComeHere == "3"):
            historyOfGhostTown()
            questioning = False
        else:
            print("Invalid Input: Try again")
            questioning = True

def ghostHunting():
    print("\n**********************************" +
        "\nGhost hunting chosen... Continue the story from here")
    
def historyOfGhostTown():
    print("\n**********************************" +
        "\nHistory of town chosen... Continue the story from here")
    
def game():
    openingTalk()
    adventureStart = input("\nGhost Town: G\nExit Game: E\n")
    if(adventureStart == "G" or adventureStart == "g"):
        ghostTown()
    elif(adventureStart == "E" or adventureStart == "e"):
        exit()
        
        
        
        
game()        