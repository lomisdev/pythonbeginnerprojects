#Test whether the number is even or odd

#Step 1: Prompt the user to enter an integer number
num = int(input("Enter an integer number: "))

#Step 2: Check whether the number is odd or even

if (num % 2) == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")