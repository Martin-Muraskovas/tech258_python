# Task 1: Waiter Helper

# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user
print("Hello User!")

# Print a list of starters
starters = ["bread", "cheeses", "breadsticks"]
print(f"Your starters for this evening are {starters[0]}, {starters[1]}, {starters[2]}")

# Take an input for the user for their starter
user_starter = input("What is your starter?")
while user_starter not in starters:
    print("sorry I do not recognize this dish")
    user_starter = input("What is your starter?")
user_starter_quantity = float(input("how many of this item would you like"))

# Print a list of mains
mains = ["chicken", "beef", "vegetarian", "vegan"]
print(f"Your mains for this evening are {mains[0]}, {mains[1]}, {mains[2]}, {mains[3]}")

# Take an input for the user for their main course
user_main = input("What is your main?")
while user_main not in mains:
    print("sorry I do not recognize this dish")
    user_main = input("What is your main?")

user_main_quantity = float(input("how many of this item would you like"))

# Print a list of desserts
deserts = ["cheesecake", "crumble", "sundae"]
print(f"Your deserts for this evening are {deserts[0]}, {deserts[1]}, {deserts[2]}")

# Take an input for the user for their dessert
user_desert = input("What would you like for desert?")
while user_desert not in deserts:
    print("sorry I do not recognize this dish")
    user_desert = input("What is your desert?")

user_desert_quantity = float(input("how many of this item would you like"))

# Print all the user's choices
user_order = [user_starter, user_main, user_desert]
print(f"You will be having {user_order[0]} as a starter")
print(f"You will be having {user_order[1]} as a main")
print(f"You will be having {user_order[2]} as a desert")

# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'
customer_order_list = [user_starter, user_main, user_desert]

# level 3
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
menu_prices = {
    "starter_prices":
        {
            "bread": 4.50,
            "cheeses": 6.00,
            "breadsticks": 3.00
        },
    "main_prices":
        {
            "chicken": 10.00,
            "beef": 11.00,
            "vegetarian": 12.00,
            "vegan": 13.00
        },
    "desert prices":
        {
            "cheesecake": 8.50,
            "crumble": 6.50,
            "sundae": 7.00
        }

}
user_starter_price = float(menu_prices["starter_prices"][user_starter]) * float(user_starter_quantity)
user_main_price = float(menu_prices["main_prices"][user_main]) * float(user_main_quantity)
user_desert = float(menu_prices["desert prices"][user_desert]) * float(user_desert_quantity)

total_bill = user_main_price + user_main_price + user_desert

print(f"Your total for the night is £{total_bill:.2f}")

# level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.


# Task 2 (optional): Password manager

# Create a program that is a mini password manager
# You will practice using dictionaries

# First, setup the ability for one user to login to the account manager using a username + password

# Once logged in, they should be able to store a usernames and passwords for different
#  accounts so they don't need to remember all their passwords
#  For example, for Facebook, email account, etc

# Once the storage is setup, add the ability to add new users to the account manager
#  (they will each need a username + password)

# Add the ability to retrieve the username and password for a specific account
#  if they input the account name e.g. hotmail

# If time - Can you make it so you need to enter the user's password before they can change it to something else?
