import random

print("Hi! Welcome to a Number Guessing Game.\nYou have 7 chances to guess the number. Lte's start!")

# Input validation for lower and upper bounds
while True:
    try:
        low = int(input("Enter the Lower bound: "))
        high = int(input("Enter the Upper bound: "))
    
        if low >= high:
           print("Error: Upper bound must be greater than Lower bound. Try again.\n")
           
        else:
          break      # Valid input exit the loop
    except ValueError:
        print("Error: Please enter valid numbers.\n")
        
print(f"You have 7 chances to guess a numberr between {low} and {high}. Let's start!\n")

while True:
    num = random.randint(low, high)
    ch = 7
    gc = 0
    guessed_correctly = False
    
    while gc < ch:
        try:
            guess = int(input('Take a guess: '))
            gc += 1
            
            if guess == num:
                print(f"Correct! The number number was {num}. You guessed in {gc} attempts.")
                guessed_correctly = True
                break
            
            elif guess > num:
                print("Too high! Try a lower number.")
                remaining = ch - gc
                if remaining > 0:
                    print(f"You have {remaining} chances remaining.\n")
                    
            else:
                print("Too low! Try a higher number.")
                remaining = ch - gc
                if remaining > 0:
                    print(f"You have {remaining} chances remaining.\n")
        except ValueError:
            print("Error: Please enter valid numbers.")
    if not guessed_correctly:
        print(f"Sorry! The number was {num}. Better luck next time.")
        
    play_again = input("\nDo you want to play again/ y/n: ")
    
    if play_again.lower() != 'y':
        print('Goodbye!')
        break
    
    
                    
                
        

        
    
    
        
