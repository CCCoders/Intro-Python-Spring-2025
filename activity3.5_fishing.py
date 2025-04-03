# Import the "random" library. This just lets us generate random numbers
import random

# Explain the premise of the game
print("Let's go fishing! Each turn you can choose an action depending on the state of the game.")
print("The goal is to catch as many fish as possible in 20 turns.")


# A "list" is like any other variable, except it can hold more than one value.
# We'll see later how to access the values in a list.

# Create a "list" of all of the available fish
available_fish = ["Salmon", "Carp", "Clown", "Swordfish", "Trout", "Bear", "Tuna", "Grouper"]

# Create a "list" for all of the fish the user has caught. It's empty at the start
caught_fish = []


# Define a function that returns the index of a random fish. An index can be used to access
# a specific value in a list
def random_fish():
    # The "len" function gets the total number of elements in a list, so len(available_fish) should
    # be the total number of available fish.
    number_of_fish = len(available_fish)
    
    # We can use "random.randint(a, b)" to get a random number from a to b. Here, we use it to get a number
    # from 1 to the number of available fish.
    random_fish = random.randint(1, number_of_fish)
    
    # The "return" keyword exits out of a function with whatever comes after "return" as the output of the function.
    # Here, our output is random_fish - 1. We have to do this because lists are "zero-indexed", meaning the index
    # number for the first element in a list is 0.
    return random_fish - 1


# Define a function for the game loop. Remember, the code inside a function doesn't execute until
# we "call" the function.
def game_loop():
    # Create a "state" variable to track the current state of the game.
    # It starts at 0, which we're treating as "idle"
    state = 0
    
    # Create a "hooked_fish" variable to track what fish is currently on the hook.
    # It starts as -1, which we're treating as no fish
    hooked_fish = -1
    
    # Create a "turn" variable to track what turn it is
    turn = 1
    
    # Keep repeating the code inside this "while" loop until turn is greater than 20 and
    # state is at least 0. This lets us exit the loop before 20 turns have passed by
    # setting state to something less than 0
    while turn <= 20 and state >= 0:
        # Print an empty new line and the current turn
        print()
        print("-- Turn", turn, "--")
        
        if state == 0:
            # The user has not cast their line yet.
            state = idle_action()

        elif state == 1:
            # The user has cast their line but hasn't gotten a bite yet.
            result = cast_action()
            # If cast_action returned a value of at least 0, save it to hooked_fish and change the state
            if result >= 0:
                hooked_fish = result
                state = 2

        elif state == 2:
            # The user casted their line and hooked a fish.
            result = hooked_action()
            if result == 1:
                # The fish was caught! Print a message, add it to the list, reset hooked_fish and state
                print("You caught a " + available_fish[hooked_fish] + "!")
                # (The "append" function just adds an element to the end of a list)
                caught_fish.append(available_fish[hooked_fish])
                hooked_fish = -1
                state = 0
            elif result == -1:
                # The user let the fish go. Print a message and reset hooked_fish and state
                print("You released a " + available_fish[hooked_fish] + ".")
                hooked_fish = -1
                state = 0
        
        # Increase the turn count by 1
        turn = turn + 1

    # When the while loop ends after 20 turns (or once state is less than 0), this function ends


# Define a function that asks the user for an action when they haven't cast their line yet.
# This returns a value corresponding to the states used in the game_loop function.
def idle_action():
    print("You're standing at the edge of the water.")
    
    # Usually you're not supposed to use a "while True" statement since that can loop forever,
    # but it's okay here because we "return" out of the function early in certain scenarios.
    # This "while" loop keeps repeating until the user enters 1 or Q
    while True:
        print("What will you do?")
        print("1: Cast your line")
        print("Q: Quit the game")
        selection = input("> ")
        
        if selection == "1":
            # If the user selected 1, exit out of this function with an output of 1.
            # This 1 corresponds to the 1 state in the game loop.
            return 1
        elif selection.lower() == "q":
            # If the user selected q, exit out of this function with an output of -1.
            # If the state in the game loop is less than 0, the game ends early.
            return -1
        else:
            # If none of the above options are selected, print an empty new line and continue the loop
            print()


# Define a function that asks the user for an action when they're waiting for a bite.
# This returns a negative value if the user didn't hook a fish, or a number corresponding
# to one of the available fish if the user did hook a fish
def cast_action():
    print("Your line is cast, but nothing has happened.")
    
    # This "while" loop keeps repeating until the user enters something to return out of the function
    while True:
        print("What will you do?")
        print("1: Wait patiently")
        print("2: Shake your fishing pole to get a fish's attention")
        print("3: Do a sad dance and hope the fish take pity")
        selection = input("> ")

        # Randomly generate a number from 0 to 100. We can use this to randomly decide the
        # outcome of the user's actions.
        roll = random.randint(0, 100)
        
        if selection == "1":
            # The user is waiting patiently. Their chance of hooking a fish is normal.

            # If the random number is at least 50, use our random_fish function to return the index of a random fish.
            # Otherwise, return -1 to keep them in the cast state.
            if roll >= 50:
                return random_fish()
            else:
                return -1
        elif selection == "2":
            # The user is shaking their fishing pole. Their chance of hooking a fish is reduced.
            
            # If the random number is at least 75, use our random_fish function to return the index of a random fish.
            # Otherwise, return -1 to keep them in the cast state.
            if roll >= 75:
                return random_fish()
            else:
                return -1
        elif selection == "3":
            # The user is dancing sadly. Their chance of hooking a fish is increased.
            
            # If the random number is at least 25, use our random_fish function to return the index of a random fish.
            # Otherwise, return -1 to keep them in the cast state.
            if roll >= 25:
                return random_fish()
            else:
                return -1
        else:
            # The user didn't select a valid option. Print an empty new line and continue the loop
            print()


# Define a function that asks the user for an action when they've hooked a fish.
# This returns 1 if the user caught a fish, 0 if the user did not, and -1 if the user gave up.
def hooked_action():
    print("You hooked a fish!")
    
    # This "while" loop keeps repeating until the user enters something to return out of the function
    while True:
        print("What will you do?")
        print("1: Reel")
        print("2: Let the fish go")
        selection = input("> ")

        if selection == "1":
            # The user is reeling in the fish

            # Randomly generate a number from 0 to 100
            roll = random.randint(0, 100)
        
            # If the random number is at least 50, return 1 to indicate the user caught the fish.
            # Otherwise, return 0.
            if roll >= 50:
                return 1
            else:
                return 0
        elif selection == "2":
            # The user let go of the fish. Return -1
            return -1
        else:
            # The user didn't select a valid option. Print an empty new line and continue the loop
            print()


# Actually run the game
game_loop()

# After the game ends, tell the user
print()
print("-- Game over! --")
print("Let's count up your fish.")

# Display all the fish that the user caught. The "i" variable tracks the index of the current fish
i = 0
while i < len(caught_fish):
    print(i + 1, "-", caught_fish[i])
    i = i + 1
    
print("Thank for playing!")
