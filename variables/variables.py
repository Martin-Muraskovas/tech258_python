# Variables

# variable_name = variable_data
a = 1   # int
b = 2   # int
c = 3.5 # float
hi = "Hello World!" # string

# print(hi)
# print(a + b)

# type method
print(type(a))
print(type(b))
print(type(c))
print(type(hi))

# Overwriting variables
x = 5
y = x
print("Before reassignment:")
print("Value of x: ", x)
print("ID of x: ", id(x))
print("Value of y: ", y)
print("ID of y: ", id(y))

x = 10
print("After reassignment:")
print("Value of x: ", x)
print("ID of x: ", id(x))

# user input
print("Hi, what is your name? ")
name = input()
print("Hi")
print(name)

