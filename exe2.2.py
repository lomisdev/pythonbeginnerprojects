#prompt the user to input a number
num = input("Enter an integer number:  ")
#Convert the string to an integer
num = int(num)

# Check whether the the integer is positive, negative or zero
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print("The number is zero.")