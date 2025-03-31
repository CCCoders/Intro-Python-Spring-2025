import curses


def main(stdscr):
    # Enable cursor blinking
    curses.curs_set(0)

    # Turn on automatic input echoing
    curses.echo()

    # Define calculator UI
    ui = [
        "+-------------------------+",
        "|                         |",  # The calculator screen where input will appear
        "+-------------------------+",
        "+-----| + |-|7|-|8|-|9|---+",
        "+-----| - |-|4|-|5|-|6|---+",
        "+-----| * |-|1|-|2|-|3|---+",
        "+-----| / |-| 0 |-| = |---+",
        "+-------------------------+"
    ]

    # Function to draw the UI
    def draw_ui():
        stdscr.clear()
        for i, line in enumerate(ui):
            stdscr.addstr(i, 0, line)
        stdscr.refresh()

    draw_ui()  # Draw the UI initially

    # Function to get user input inside the calculator screen
    def get_input():
        curses.curs_set(1)  # Make cursor visible
        stdscr.move(1, 2)  # Move cursor inside the calculator display
        stdscr.refresh()
        user_input = ""

        while True:
            key = stdscr.getch()

            if key in (10, 13):  # Enter key pressed
                break
            elif key in (8, 127, curses.KEY_BACKSPACE):  # Backspace
                if len(user_input) > 0:
                    user_input = user_input[:-1]
            elif chr(key).isdigit() or chr(key) in "+-*/" or chr(key) == '.':  # Allow numbers & operators
                user_input += chr(key)

            # Update display
            stdscr.addstr(1, 2, " " * 16)  # Clear input area
            stdscr.addstr(1, 2, user_input)  # Show updated input
            stdscr.refresh()

        return user_input.strip()

    # Get input expression (e.g., "7+3")
    draw_ui()
    stdscr.addstr(1, 2, "Enter equation:")
    stdscr.refresh()

    expression = get_input()

    try:
        result = eval(expression)  # Compute the result
    except Exception:
        result = "Error"

    # Show result inside the calculator screen
    draw_ui()
    stdscr.addstr(1, 2, f"{expression} = {result}")
    stdscr.refresh()

    stdscr.getch()  # Wait for key press before exiting


# Run the curses application
while(True):
    curses.wrapper(main)
