"""This program converts kilometers to miles
but first it verifies if the input is numeric 
and whether it is posive inorder to proceed"""
#Prompt user to enter distance in kilometers
km_iput = input("Enter distance in kilometers: ")

#Check if the input is numeric
if km_iput.isnumeric():
    km = int(km_iput)
    #Check whether the input is positive
    if km > 0:
        #Convert kilometers to miles (1 km ~ 0.621371)
        miles = km * 0.621371
        print(f"{km} kilometers converted to miles is {miles:.2f} miles.")
    else:
        #Do nothing if input is negative
        print("Please enter a positive number.")
else:
    #Do nothing if the input is not a number
    print("Invalid input. Please enter a valid number.")
