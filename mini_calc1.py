"""
mini calculator 1.0
Created by saint
This program takes numbers from users and performs operations based on the operator they choose
"""
while True:
    #Get the first number from user and convert it to float so we can handle it in decimals  a
    num1 = float(input("Enter the first number: "))
    #Get the operator to use
    operator = input("Enter operator (+, -, *, /): ")
    #Get the second number from user and convert it to float to aloow decimal input
    num2 = float(input("Enter the second number: "))
    #Check the operator and perform operations based on it
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        #This block is executed if the operator chosen is not on the list
        print("Invalid operator!")
     #Ask the user if they want t perform another calculation   
    choice = input("Do you wanna calculate again? y/n:").lower()
    if choice != "y":
        #if not, give a goodbye message and stop the program
        print("Goodbye!")
        break