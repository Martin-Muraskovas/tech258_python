# Sets and Frozen sets

# Create a set

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Sets are UNORDERED and UN-INDEXED

# Add an element
fruits.add("orange")
print(fruits)

# Remove an element
fruits.remove("apple")
print(fruits)

# Attempt to add a duplicate - there can be no duplicates in a set
fruits.add("banana")
print(fruits)

# Convert a list to a set to remove a duplicate
example = ["one", "two", "three", "one"]
no_dupes = set(example)
print(no_dupes)


int_set = {1, 2, 3, 4, "string"}
print(int_set)

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

print(set_a | set_b)
print(set_a - set_b)

# frozen set --> IMMUTABLE SET

frozen_set = frozenset(["hello", "world"])
print(frozen_set)
# frozen_set.add("!") cant add because immutable

normal_set = {"let's", "learn"}
normal_set.add(frozen_set)
print(normal_set)
