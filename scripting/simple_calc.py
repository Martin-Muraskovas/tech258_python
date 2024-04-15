# Simple calculator functions
from math_operators import add, subtract, divide, multiply

# import math_operators
# from math_operators import *


first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

result_1 = add(first_num, second_num)
result_2 = subtract(first_num, second_num)
result_3 = multiply(first_num, second_num)
result_4 = divide(first_num, second_num)

# result = math_operators.add(first_num, second_num)

print(f"{first_num} + {second_num} = {result_1}")
print(f"{first_num} - {second_num} = {result_2}")
print(f"{first_num} * {second_num} = {result_3}")
print(f"{first_num} / {second_num} = {result_4}")


# A package is multiple modules bundled into one.

# Library = catch all term.
