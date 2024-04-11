# Bools and None

# Booleans can be: True or False

a = True
b = False

# print(a == b)  # False
# print(a != b)  # False
#
# # False is ALWAYS 0
# print(a >= b)  # True
# print(a <= b)  # False

# Boolean methods

# hi = "Hello World"
#
# # We can use these to make decisions
# print(hi.isalpha())  # False
# print(hi.islower())  # False
# print(hi.isupper())  # False
# print(hi.endswith("d"))  # True
# print(hi.startswith("H"))  # True

# What happens when you try to convert a string to a bool using casting?

# # Always True unless the string is empty
# print(bool("a"))  # True
# print(bool(""))  # False
#
# # What happens when we convert a number to a bool
#
# # Always True unless the string is 0
# print(bool(0))  # False - Only 0 can be false
# print(bool(40))  # True

# The value of None

# None is an object, it is essentially a placeholder

# None when converted to a bool is False
print(bool(None))

# None != False

x = None

print(x == False)
print(x == None)

print(type(x))

# None is best used over an empty string etc.
