# # Strings
#
# single_quotes = 'Single quotes'
# double_quotes = "Double quotes"
#
# print(single_quotes, double_quotes)
#
# # Double quotes better because single looks like apostrophe
#
# # bad_string = 'It's not right'
# good_string = "It's not right"
# print(good_string)
#
# # If you really want to use single quotes
# escape_example = 'I said \'Wow!\''
# print(escape_example)

# String Slicing

# Hw = "Hello World!"
#
# # find out how many characters are in this string using an inbuilt python method
# print(len(Hw))
#
# # Target just the first character using string slicing
# print(Hw[0])
#
# # Target the last character using string indexing
# print(Hw[11])
# # print(Hw[-1])  # Get the last character of any string
#
# # Use negative indexing to get the second to last character
# print(Hw[-2])
#
# # Bonus: String slice to get the first 3 characters
# print(Hw[0:3])

# # String methods
# white_space = "Lot's of white space at the end         "
# print(len(white_space))
# print(len(white_space.strip()))

example_string = "Here's some text with lot's of text"
# Count a substring within a string
print(example_string.count("text"))

# Make a string lowercase
print(example_string.lower())

# Make a string uppercase
print(example_string.upper())

# Make a string capitalised
print(example_string.capitalize())

# Replacing text
print(example_string.replace("with ", ","))

# Concatenation and Casting
a = "here "
b = "more "
c = "much more"
print(a + b + c)

x = 2
y = 5.4
z = " theres now a number 2 5.4 unless we put a space in!"
w = "30"

print(str(x) + " " + str(y) + z)
print(x + y + int(w))

# F-strings

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm} cm tall")

name = "Snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS")

# using f-strings to format numbers

pi = 3.14159265359

# Use an f-string to print pi to 3 dp
print(f"{pi.__round__(3)}")
# Use an f-string to print pi to 5 dp
print(f"{pi.__round__(5)}")

print(f"{round(pi,3)}")
print(f"{pi:.3f}")


score = 16
max_score = 26

print(f"You scored {score/max_score:.2%}")
print(f"You scored {score/max_score:.0%}")

