# mixture = [1, 2, 3, "one", "two", "three"]
# print(mixture)
#
# 1. Use your code from the "Task: Get name, age and DOB details from a user".
name = str(input("What is your name?"))
age = int(input("What is your age?"))
dob = str(input("What is your DOB (DD/MM/YYYY)"))

# 2. Mix the name, age and DOB into one list user_details_list
details = [name, age, dob]

# 3. Print the user's name, age and DOB from the list
print(f"Your name is {str(details[0]).capitalize()}, your age is {details[1]}, and your Date of Birth is {details[2]}")

# 4. Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
print(f"The data type of age is {type(details[1])}")

# 5. Ask the user for their height in cm and save it to the variable height
height = float(input("What is your height in cm?"))

# 6. Save height as a float in the list, and print the height from the list.
details.append(float(height))
print(f"Your height is {details[3]}cm")

