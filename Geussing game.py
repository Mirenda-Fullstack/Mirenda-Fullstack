import random


def guessing_game():
    print("\033[1mWelcome to my Guessing Game\033[0m\n")

    # Flag to track if the very first game has been played from the main menu or not.
    # False: It's the first time "Start game" is selected, so the mode is random (unlimited/limited).
    # True: It's a subsequent "Start game" selection, so the mode is always limited.
    first_time_playing = False

    # Variable to hold the number of attempts for limited games.
    # Its value will be set dynamically when a limited game starts.
    number_of_attempts = 0

    while True:  # This is the main menu loop
        print("\n---Main menu---\n")
        print("1. Start game")
        print("2. View rules")
        print("3. Quit\n")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            print("\nStarting game...")
            # The computer guesses a number between 1 and 100
            computer_choice = random.randint(1, 100)

            # Determine Game Mode for this round
            # If it's the very first time playing from the main menu,
            # randomly decide if it's an unlimited or limited game.
            if not first_time_playing:
                # Randomly choose if the first game will be unlimited or limited.
                # True means limited, False means unlimited.
                is_limited_game = random.choice([True, False])
                first_time_playing = True  # Mark that the initial game decision has been made.
            else:
                # For subsequent plays (after the very first one), it's always limited.
                is_limited_game = True

            # If it's a limited game, set the number of attempts for this round.
            # For each new limited game, the number of attempts will be a new random value.
            if is_limited_game:
                number_of_attempts = random.randint(3, 8)  # Set a random number of attempts between 3 and 8
                print(f"Here you have a limited number of attempts! Use them wisely!\nYou have \033[1m{number_of_attempts}\033[0m attempts.")
            else:
                print("Here you have an unlimited number of attempts! Guess until you get it right!")

            # --- Game Play Loop ---
            attempts_made = 0  # Counter for attempts made in the current game round
            game_over = False  # Flag to indicate if the current game round has concluded (win/lose)

            # This loop handles a single game round (either unlimited or limited guesses)
            while True:
                #Check for the condition when the game will be lose before asking fo the guess
                if is_limited_game and attempts_made >= number_of_attempts:
                    print(f"\nSorry, your attempts are over, YOU LOOSE! The number was \033[1m{computer_choice}\033[0m.")
                    game_over = True
                    break  # Exit the guessing loop (player lost)

                try:
                    if is_limited_game:
                        user_input = int(input(f"Enter a number between 1 and 100:\n"))
                    else:
                        user_input = int(input(f"Enter a number between 1 and 100:\n"))

                    if user_input < 1 or user_input > 100:
                        print("Please enter a number within the 1 to 100 range.")
                        # Do not count this as an attempt, continue to next loop iteration
                        continue

                        # Increment attempts only after valid input (and within range)
                    attempts_made += 1

                    # Compare user's guess with computer's choice
                    if user_input > computer_choice:
                        print("Enter a lower number please.")
                        # Display remaining attempts if limited game and not won yet
                        if is_limited_game and not game_over:
                            print(f"You have \033[1m{number_of_attempts - attempts_made}\033[0m attempts left.")
                    elif user_input < computer_choice:
                        print("Enter a higher number please.")
                        # Display remaining attempts if limited game and not won yet
                        if is_limited_game and not game_over:
                            print(f"You have \033[1m{number_of_attempts - attempts_made}\033[0m attempts left.")
                    else:  # user_input == computer_choice (WIN condition)
                        print(f"\nCongratulations! You won!!! The number was \033[1m{computer_choice}\033[0m.")
                        print(f"You guessed it in \033[1m{attempts_made}\033[0m attempt(s).")
                        game_over = True
                        break  # Exit the guessing loop (player won)

                except ValueError:
                    print("Invalid input. Please enter a whole number.")
                    # Do not count invalid input as an attempt, continue to next loop iteration
                    continue

            #When the game_over is false before this line can execute
            if game_over:
                play_again_response = input("\nDo you want to play again? (y/n): ").lower()
                if play_again_response == "n":
                    print("Press enter to return to the main menu.")
                    break  # Exit the outer `while True` (main menu) loop

        elif user_choice == "2":
            print("\n--- Game Rules ---")
            # Corrected rule to match actual game range (1-100)
            print("1. The computer will choose a random a number between 1 and 100.")
            print("2. Your goal is to guess that number.")
            print("3. After each guess, you will be told if your number is too high or too low.")
            print("4. The very first game will randomly be either unlimited or limited attempts depending on if it's your first time playing or not.")
            print("5. All subsequent games will have a random, limited number of attempts.")
            print("6. The game ends when you guess the correct number or use all your of attempts.\n")
            input("Press Enter to return to the main menu")

        elif user_choice == "3":
            print("Thank you for playing! Goodbye.")
            break  # Exit the main menu loop

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

guessing_game()

