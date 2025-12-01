while True:
    try:
        age = int(input("Enter you age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age > 120:
            print("That seems unrealistic!")
        else:
            print(f"You are {age} years old.")
    except ValueError:
        print("Error: Please enter a valid number for age.")
        #inner validation loop
    while True:
        confirm = input("Do you want to confirm? (y/n): ").lower()
        if confirm in ["y", "n"]:
             break
        print("Invalid choice. Please type 'y' or 'n'.")
       
    if confirm == "n":
        print("Goodbye! Stay curious G.")
        break
        
        