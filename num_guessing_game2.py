import random

print("Hi! Welcome to the Number Guessing Game 🎯")
print("You have 7 chances to guess the number. Let's start!\n")

# Input validation for bounds
while True:
    try:
        low = int(input("Enter the lower bound: "))
        high = int(input("Enter the upper bound: "))
        if low >= high:
            print("Error: Lower bound must be less than upper bound. Try again.\n")
        else:
            break
    except ValueError:
        print("Error: Please enter valid numbers.\n")

def play_game(low, high):
    num = random.randint(low, high)
    attempts = 7

    for i in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {i}/{attempts}: Take a guess → "))
            if guess < low or guess > high:
                print(f"Out of range! Please guess between {low} and {high}.")
                continue

            if guess == num:
                print(f"🎉 Correct! The number was {num}. You guessed it in {i} attempt(s)!\n")
                return True
            elif guess > num:
                print("Too high! Try a lower number.")
            else:
                print("Too low! Try a higher number.")

            remaining = attempts - i
            if remaining > 0:
                print(f"You have {remaining} chance(s) left.\n")

        except ValueError:
            print("Error: Please enter a valid integer.\n")

    print(f"❌ Sorry! The number was {num}. Better luck next time.\n")
    return False

# Main loop
while True:
    play_game(low, high)
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again not in ('y', 'yes'):
        print("Goodbye 👋")
        break
