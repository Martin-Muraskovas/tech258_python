# Task 1: Create a BMI program

# Get the user's height and weight
weight = float(input("What is your weight in kilograms?"))
height = float(input("What is your height in meters?"))

# Calculate their BMI from the height and weight given
user_bmi = weight / (height * height)

# Print the BMI as a message to the user
print(f"Your BMI is {user_bmi:.2f}")

# Task 2: Create a tip calculator using below pseudocode

# Let's help with generating a bill with tips added and allow the user to split among a number of people

# Get the bill from the user
initial_bill = float(input("What is the total bill?"))

# Calculate the tip (assume a percentage of 10-15%)
tip = initial_bill * 0.15

# Calculate bill with the tip added
total = initial_bill + tip
# I would combine these and just do total = initial_bill * 1.15

# Ask how many people they want to split with
party_size = input("How many people are you splitting the bill with?")

# Calculate the bill divided by the split amount
bill_per_person = total / float(party_size)

# Print the split bill per person, being rounded to 2 decimal places
print(f"The amount each person should pay is £{bill_per_person:.2f}")
