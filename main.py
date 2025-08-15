import random  # For generating a random number

def main():
    """
    Main game loop that handles replaying rounds.
    """
    while True:
        # Play one round of the game
        game_completed = play_one_round()

        # If the user quit mid-round, exit the whole game
        if not game_completed:
            break  

        # Ask if the player wants to play again
        wanna_play = input("Would you like to play again? (yes/no): ").strip().lower()
        if wanna_play != "yes":
            print("Thanks for playing. Goodbye!")  # Farewell message
            break  # Exit main loop and end program

def play_one_round() -> bool:
    """
    Plays one round of the game.
    Returns True if user completed the round,
    False if they quit.
    """
    computer_choice = random.randint(1, 100)   # Random number between 1 and 100
    score = 100   # Starting score

    while True:
        # Ask the player for their guess
        user_guess = input("Please enter your guess number (between 1 and 100) or 'q' to quit: ")

        # If the input is a number
        if user_guess.isdigit():
            user_guess = int(user_guess)  # Convert input to integer

            # Check if guess is in range
            if user_guess < 1 or user_guess > 100:
                print("Your guess is out of range. Please choose a number between 1 and 100.")
                continue

            # Compare guess to computer's number
            elif user_guess > computer_choice:
                print("It is much higher than my choice. Please try again.")
                score -= 10  # Deduct points

            elif user_guess < computer_choice:
                print("It is much lower than my choice. Please try again.")
                score -= 10  # Deduct points

            else:
                # # Correct guess
                print("You win!")
                print(f"Your score is: {score}")
                return True  # User finished the round successfully

        # If the player wants to quit
        elif user_guess.lower() == 'q':
            print("Thanks for playing the game. Have a nice day!")
            return False  # User quit the game

        # If input is invalid
        else:
            print("Invalid input. Please enter a number between 1 and 100 or 'q' to quit.")


if __name__ == "__main__":
    main()   # Start the game
