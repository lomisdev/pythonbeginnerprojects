import random

print("Hi! Welcome to a Number Guessing Game.\nYou have 7 chances to guess the number. Lets start!.")

# Input validation for lower and upper bounds

while True:
    try:
        low = int(input("Enter the lower bound: "))
        high = int(input("Enter the upper bound: "))
        
        if low >= high:
            print("Error: Lower bound cannot be greater or equal to upper bound. Please try again.\n")
        else:       # Valid input exit loop
            break
    except ValueError:
        print("Error: Please enter valid numbers.")
    
print(f"You have 7 chances to guess the number between {low} and {high}. Lets start!.\n")
    
while True:
    num = random.randint(low, high)
    gl = 7               # Allowed guess times
    gc = 0               # Guess counter
    guessed_correctly = False
    
    while gc < gl:
        try:
            guess = int(input("Take a guess: "))
            gc += 1   # Increament guess counter 
            
            # Check whether the guess is correct
            if guess == num:
                print(f"Correct! The number was {num}. You guessed it in {gc} attempt(s).\n")
                guessed_correctly = True
                break
            
            elif guess > num:
                print("Too high! Try a lower number.")
                remaining = gl - gc   # To count remaining chances
                if remaining > 0:
                    print(f"You have {remaining} chances remaining.\n")
                    
            else:
                print("Too low! Try a higher number.")
                remaining = gl - gc   # To count remaining chances
                if remaining > 0:
                    print(f"You have {remaining} chances remaining.\n")
        except ValueError:
            print("Error: Please enter valid numbers.")
    if not guessed_correctly:
        print(f"Sorry! The number was {num}. Better luck next time.")
    
    # Ask if user wants to play again
    play_again = input("Do you want to play again? y/n: ")
    # Evaluate user input 
    if play_again.lower() != 'y':
        print("Goodbye!")
        break
    
                    
                    
            
            