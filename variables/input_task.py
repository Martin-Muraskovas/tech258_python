# Prompt the user to get the input on the same line you greet them
# Can you print the returned message all on one line?


name = str(input("What is your name?"))
age = str(input("What is your age?"))

print("Your name is", name, "Your age is", age)

house_number = str(input("What is your house number?"))
house_street = str(input("What is your street name?"))

print("You live at house number", house_number, "on", house_street)

hobby = str(input("What is an activity that you like to do in your free time?"))

print("Wow!", name, "aged", age + ", it must be fun to do", hobby, "at house number", house_number, "on", house_street)
print(f"you must not like your neighbor at house number {int(house_number) + 1}")

print(type(name), type(age), type(hobby), type(house_number), type(house_street))
