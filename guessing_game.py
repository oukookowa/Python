#Generates a randonm integer between 1 and 10 and matches it against users's guess
import random

# Generate a secret number
secret_number = random.randint(1, 10)

while True:
    # Get user's guess
    guess = int(input("Guess the number (between 1 and 10): "))
    
    # Match the guess with the secret number
    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")
            break
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")

# Offer to play again
play_again = input("Do you want to play again? (yes/no): ").strip().lower()
if play_again == 'yes':
    # Restart the script
    secret_number = random.randint(1, 10)
    while True:
        guess = int(input("Guess the number (between 1 and 10): "))
        match guess:
            case _ if guess == secret_number:
                print("Congratulations, you guessed it!")
                break
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
else:
    print("Thanks for playing!")
