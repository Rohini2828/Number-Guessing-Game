import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        try:
            # Take user input
            user_guess = int(input("Make a guess: "))
            
            # Increment the number of attempts
            attempts += 1
            
            # Check if the guess is correct, too high, or too low
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                
        except ValueError:
            print("Invalid input! Please enter a number.")
    
# Start the game
if __name__ == "__main__":
    number_guessing_game()
