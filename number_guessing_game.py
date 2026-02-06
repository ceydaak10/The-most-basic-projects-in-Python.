import random

def number_guessing_game():
    secret_number = random.randint(1, 30)
    attempts_left = 3
    
    print("Welcome to this easy number guessing game!")
    print("I have picked a number between 1 and 30. Can you guess it?")
    
    while attempts_left > 0:
        # Get the user's guess
        guess = int(input(f"\nEnter your guess (Attempts left: {attempts_left}): "))
        
        if guess == secret_number:
            print("Congratulations, you got it! 🎉")
            break
        
        attempts_left -= 1
        
        if attempts_left == 0:
            print(f"Sorry, you're out of attempts! The secret number was {secret_number}. 😔")
        else:
            if guess < secret_number:
                print("Try a higher number! I'm sure you'll find it.")
            elif guess > secret_number:
                print("Try a lower number! It's not that hard.")

# Call the function to start the game
number_guessing_game()
             
             
             
      
    
        


