#Ask the user for the two strings
first_name = input('what is your first name?: ')
last_name = input('what is your alst name?: ')

#Concatenate with a space and store them in new_string
new_string = first_name + " " + last_name

#print the value of new_string
print("Combined string:", new_string)

#print the length of the new string
print("Length of combined string:", len(new_string))

#Convert to uppercase and store in a new variable 
upper_case = new_string.upper()
print("Uppercase version:", upper_case )

#Check if Albus is in the uppercase version
if 'ALBUS' in upper_case:
    print("The string contains 'Albus'")

else:
    print("The string does not contain 'Albus'")




