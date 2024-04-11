# Guidelines
#
# Define a dictionary called story1. It should have the following keys:
# 'start', 'middle' and 'end'
# Print the entire dictionary
# Print the type of your dictionary
# Print only the keys
# Print only the values
# Print the individual values using the keys (individually, lots of print commands)
# Now, let's add a new key:value pair:
# 'hero': yourSuperHero
# Hints:
#
# THE MORE CREATIVE THE BETTER
# If you finish early, try to make the story a choose your own adventure type of program.


story1 = {
    "start": "The onion man was born in the year 1902.",
    "middle": "He had to battle with the shallot man for the title of 'The Layered Slayer'",
    "end": "He defeated the shallot man in a duel by caramelizing the shallots using butter and vegetable oil"
}

print(story1)
# print(f"{story1["start"]}\n{story1["middle"]}\n{story1["end"]}")

print(type(story1))

print(story1.keys())

print(story1.values())

print(story1["start"])
print(story1["middle"])
print(story1["end"])

# for values in story1.values():
#     print("using for loop", values)

story1["hero"] = "Onion Man"
