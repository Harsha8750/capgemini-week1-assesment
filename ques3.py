import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while not guessed:
        # Get user's guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Too Low!")
        elif user_guess > number_to_guess:
            print("Too High!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            guessed = True

# Start the game
number_guessing_game()
