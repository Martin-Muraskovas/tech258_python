# Python Standard Library

# The standard library consists of many modules and packages that are very useful and thus added to python by default.

import random
import math
import os
import datetime
import builtins
import requests

# Random demo:

# print(random.random())
# print(random.randrange(1, 10))

# Math demo:

# num_float = 23.66
# print(math.ceil(num_float))
# print(math.floor(num_float))
# print(math.pi)
# print(f"Remainder from 1/5: {math.remainder(1, 5)}")

# OS demo

# returning current working directory
# working_dir = os.getcwd()
# print(f"Current working directory: {working_dir}")
#
# # get user
# username = os.environ.get("USERNAME") or os.environ.get("USER")
# print(f"Username is: {username}")
#
# # cpu cores
# cpu_cores = os.cpu_count()
# print(f"Amount of CPU cores: {cpu_cores}")
#
# # make directory
# os.mkdir("test_dir")

# datetime demo

# print(f"Today's date is: {datetime.datetime.today()}")

# builtins demo
# for name in dir(builtins):
#     if name[0].islower():
#         print(name)

# requests demo
requests_bbc = requests.get("https://www.bbc.co.uk/")
print(requests_bbc.status_code)
print(requests_bbc.content)
