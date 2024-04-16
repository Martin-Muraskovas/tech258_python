import requests
import json
import random

total_pokemon = 1025
cpu_choice = random.randint(1, total_pokemon)
cpu_poke_dict = requests.get("https://pokeapi.co/api/v2/pokemon/"+f"{cpu_choice}")

user_pokemon_name = input("What pokemon would you like to battle with?")
user_poke_dict = requests.get("https://pokeapi.co/api/v2/pokemon/"+f"{user_pokemon_name}")
user_poke_data = json.loads(user_poke_dict.text)

cpu_poke_data = json.loads(cpu_poke_dict.text)

print(f"{cpu_poke_data["name"]} is battling {user_poke_data["name"]}\n")
# print(user_poke_data)

user_moves = user_poke_dict.json()["moves"]
user_move_names = [move["move"]["name"] for move in user_moves]

user_first_move = random.randint(0, len(user_move_names)-1)
user_second_move = random.randint(0, len(user_move_names)-1)
user_third_move = random.randint(0, len(user_move_names)-1)
user_fourth_move = random.randint(0, len(user_move_names)-1)


user_moves_and_stats = {
    "user_health": random.randint(30, 250),
    "user_move1_damage": random.randint(10, 70),
    "user_move2_damage": random.randint(10, 70),
    "user_move3_damage": random.randint(10, 70),
    "user_move4_damage": random.randint(10, 70)
}


cpu_moves = cpu_poke_dict.json()["moves"]
cpu_move_names = [move["move"]["name"] for move in cpu_moves]

cpu_first_move = random.randint(0, len(cpu_move_names)-1)
cpu_second_move = random.randint(0, len(cpu_move_names)-1)
cpu_third_move = random.randint(0, len(cpu_move_names)-1)
cpu_fourth_move = random.randint(0, len(cpu_move_names)-1)

cpu_moves_and_stats = {
    "cpu_health": random.randint(30, 250),
    "cpu_move1_damage": random.randint(10, 70),
    "cpu_move2_damage": random.randint(10, 70),
    "cpu_move3_damage": random.randint(10, 70),
    "cpu_move4_damage": random.randint(10, 70)
}

print("==== CPU Moves ====")
print("1." + cpu_move_names[cpu_first_move])
print("2." + cpu_move_names[cpu_second_move])
print("3." + cpu_move_names[cpu_third_move])
print("4." + cpu_move_names[cpu_fourth_move])
print("\n")

cpu_health = cpu_moves_and_stats["cpu_health"]
user_health = user_moves_and_stats["user_health"]

while cpu_health > 0 and user_health > 0:
    print()
    cpu_move_used = random.randint(1, 4)
    print(f"Gary's {cpu_poke_data["name"]}'s health is {cpu_health}\n")
    print(f"Red's {user_poke_data["name"]}'s health is {user_health}")
    print("====  User Moves ====")
    print("1." + user_move_names[user_first_move].capitalize() + f" {user_moves_and_stats["user_move1_damage"]} Damage")
    print("2." + user_move_names[user_second_move].capitalize() + f" {user_moves_and_stats["user_move2_damage"]} Damage")
    print("3." + user_move_names[user_third_move].capitalize() + f" {user_moves_and_stats["user_move3_damage"]} Damage")
    print("4." + user_move_names[user_fourth_move].capitalize() + f" {user_moves_and_stats["user_move4_damage"]} Damage")
    user_move_used = input("What move are you going to use? ")
    if user_move_used == "1":
        cpu_health = cpu_health - user_moves_and_stats["user_move1_damage"]
    elif user_move_used == "2":
        cpu_health = cpu_health - user_moves_and_stats["user_move2_damage"]
    elif user_move_used == "3":
        cpu_health = cpu_health - user_moves_and_stats["user_move3_damage"]
    elif user_move_used == "4":
        cpu_health = cpu_health - user_moves_and_stats["user_move4_damage"]
    else:
        user_move_used = input("Invalid input! What move are you going to use? ")
    print(f"\nGary's {cpu_poke_data["name"]} health is {cpu_health}")

    if cpu_move_used == 1:
        user_health = user_health - cpu_moves_and_stats["cpu_move1_damage"]
    elif cpu_move_used == 2:
        user_health = user_health - cpu_moves_and_stats["cpu_move2_damage"]
    elif cpu_move_used == 3:
        user_health = user_health - cpu_moves_and_stats["cpu_move3_damage"]
    elif cpu_move_used == 4:
        user_health = user_health - cpu_moves_and_stats["cpu_move4_damage"]
    print(f"Red's {user_poke_data["name"]} health is {user_health}")

if user_health <= 0 and cpu_health <= 0:
    print("Red Wins!")
elif user_health > cpu_health and cpu_health <= 0:
    print("Red Wins!")
else:
    print("Gary Wins!")

# https://pokeapi.co/api/v2/ability/{id or name}/
