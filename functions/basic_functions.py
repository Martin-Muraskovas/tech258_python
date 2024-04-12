# Functions

# DRY - Don't Repeat Yourself

# function with no arguments

def print_something(name):
    print(f"Hello my name is {name}")


print_something("Martin")


# function with args

# def addition(int1, int2):
#     return int1 + int2
#
#


# default arguments

def addition(int1=2, int2=2):
    return int1 + int2


print(addition())
print(addition(5, 7))
print(addition(int2=14))


# multiple arguments

def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)


multi_args(1, 2, 3, 4, 5, )
multi_args(1, 2, 3)


# type hints

def division(denom: int, num: int) -> float:
    return denom / num


print(division(10, 5))
