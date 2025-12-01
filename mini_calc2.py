"""
Mini Calculator 2.0
Created by Saint
This version adds user validation and error handling
"""
while True:
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, **, /): ")
        num2 = float(input("Enter the second number: "))
        
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "**":
            print(num1 ** num2)
        elif operator == "/":
            if num2 != 0:
                print(num1 / num2)
            else:
                print("Cannot divide by zero!")
        else:
            print("Invalid operator!")
    except ValueError:
        print("Error: Please enter valid numbers only.")
        
    choice = input("Do you want to calculate again? y/n: ")
    if choice != "y":
        print("Goodbye")
        break
        