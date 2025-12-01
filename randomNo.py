#Number Guessing Game 2.0
#Created by Saint
#This program picks a random number and lets user guess it in 3 tries
  
import random #import the randome module to generate random numbers

while True:
    #Generate a random secret number between 1 and 10
    secret_number = random.randint(1, 10)
    #Initialize counters for guesses
    guess_count = 0
    guess_limit = 3
    
    print("I'm thinking of a number between 1 and 10...")
    #Loop until until user runs out of guesses
    while guess_count < guess_limit:
        #Ask for user input
        guess = int(input("Take a guess: "))
        guess_count += 1 #Increament guess counter
        
        #Check if guess is correct
        if guess == secret_number:
            print("Congratulations! You got it!")
            break
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")
    else:
        #This runs if the loop finishes without a 'break'
        print(f"Out of tries! The secret number was {secret_number}")

    #Ask if the user wants to play again
    play_again = input("Play again? y/n: ").lower()
    if play_again != "y":
        print("Goodbye! Goodgame.")
        break    